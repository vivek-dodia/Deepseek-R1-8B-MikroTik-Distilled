# Repository Information
Name: Mikrotik-rust

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/zhangmaku/Mikrotik-rust.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: .travis.yml
================================================
language: rust
================================================

File: README.md
================================================
Router Os
================
Mikrotik API for Rust
This API gives you the ability to connect to your mikrotik router over a tcp connection.
[![Build Status](https://travis-ci.org/Wooowe/Mikrotik-rust.svg?branch=master)](https://travis-ci.org/Wooowe/Mikrotik-rust) [![Latest Version](https://img.shields.io/badge/crates.io-0.0.21-orange.svg)](https://crates.io/crates/routeros_rust)
### Installation
Add router_os via your `Cargo.toml`:
```toml
[dependencies]
routeros_rust = "*"
```
#### or
```toml
[dependencies.routeros_rust]
git = "https://github.com/Wooowe/mikrotik-rust"
```
### Usage
```rs
extern crate router_os;
use router_os::ApiRos;
use std::net::TcpStream;
fn main() {
    let mut stream = TcpStream::connect("192.168.1.1:8728").unwrap();
    let mut apiros = ApiRos::new(&mut stream);
    apiros.login("admin".to_string(), "".to_string());
    apiros.write_sentence(vec!["/ip/address/print".to_string()]);
    loop {
        let reply = apiros.read_sentence();
        if reply.len() == 0 {
            continue;
        }
        if reply[0] == "!done" {
            break;
        }
    }
}
```
================================================

File: routeros.rs
================================================
#![crate_name = "router_os"]
#![crate_type = "lib"]
extern crate crypto;
use crypto::md5::Md5;
use crypto::digest::Digest;
use std::collections::BTreeMap;
use std::io::prelude::*;
use std::net::TcpStream;
fn hex_binascii<'a>(hexstr: String) -> Result<Vec<u8>, &'a str> {
	if hexstr.len() % 2 != 0 {
		Err("Odd number of characters")
	}else {
		let mut result: Vec<u8> = Vec::new();
		let mut i = 0;
		let c_hexstr: Vec<char> = hexstr.chars().collect();
		while i < c_hexstr.len()-1 {
		    let top = c_hexstr[i].to_digit(16).unwrap() as u8;
		    let bottom = c_hexstr[i+1].to_digit(16).unwrap() as u8;
		    let r = (top << 4) + bottom;
			result.push(r);
		    i += 2;
		}
		Ok(result)
	}
}
pub struct ApiRos<'a> {
	stream: &'a mut TcpStream,
}
impl<'a> ApiRos<'a> {
	pub fn new(s: &'a mut TcpStream) -> ApiRos<'a> {
		ApiRos {
			stream: s
		}
	}
	pub fn try_read(&mut self) -> bool {
		if self.stream.read(&mut [0]).unwrap() > 0 {
			true
		}else {
			false
		}
	}
    fn write_str(&mut self, str_buff: &[u8]) {
        match self.stream.write(str_buff) {
            Ok(_) => {}
			Err(e) => { panic!("connection closed by remote end, {}", e); }
		}
	}
    fn read_str(&mut self, length: usize) -> String {
        let mut buff: Vec<u8> = Vec::new();
        for _ in 0 .. length {
			let mut tmp_buff: [u8; 1] = [0];
			match self.stream.read(&mut tmp_buff) {
				Ok(_) => {}
				Err(e) => { panic!("connection closed by remote end, {}", e); }
			}
			buff.push(tmp_buff[0]);
		}
		String::from_utf8(buff).unwrap()
	}
	fn write_len(&mut self, len: u32) {
        if len < 0x80 {
            self.write_str(&[len as u8]);
		} else if len < 0x4000 {
            let l = len | 0x8000;
            self.write_str( &[((l >> 8) & 0xFF) as u8] );
            self.write_str( &[(l & 0xFF) as u8] );
		} else if len < 0x200000 {
            let l = len | 0xC00000;
            self.write_str( &[((l >> 16) & 0xFF) as u8] );
            self.write_str( &[((l >> 8) & 0xFF) as u8] );
            self.write_str( &[(l & 0xFF) as u8] );
		} else if len < 0x10000000 {
            let l = len | 0xE0000000;
            self.write_str( &[((l >> 16) & 0xFF) as u8] );
            self.write_str( &[((l >> 24) & 0xFF) as u8] );
            self.write_str( &[((l >> 8) & 0xFF) as u8] );
            self.write_str( &[(l & 0xFF) as u8] );
		} else {
            self.write_str( &[(0xF0) as u8] );
            self.write_str( &[((len >> 24) & 0xFF) as u8] );
            self.write_str( &[((len >> 16) & 0xFF) as u8] );
            self.write_str( &[((len >> 8) & 0xFF) as u8] );
            self.write_str( &[(len & 0xFF) as u8] );
		}
	}
    fn read_len(&mut self) -> u32 {
        let mut c: u32 = self.read_str(1).as_bytes()[0] as u32;
        if c & 0x80 == 0x00 {
		} else if c & 0xC0 == 0x80 {
            c &= !0xC0;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
		} else if c & 0xE0 == 0xC0 {
            c &= !0xE0;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
		} else if c & 0xF0 == 0xE0 {
            c &= !0xF0;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
		} else if c & 0xF8 == 0xF0 {
            c = self.read_str(1).as_bytes()[0] as u32;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
            c <<= 8;
            c += self.read_str(1).as_bytes()[0] as u32;
            c += self.read_str(1).as_bytes()[0] as u32;
            c <<= 8;
		}
		c
	}
	fn read_word(&mut self) -> String {
		let len = self.read_len();
		let ret = self.read_str(len as usize);
		if len > 0 { println!(">>> {}", ret); }
		ret
	}
	fn write_word(&mut self, w: String) {
		if w.len() > 0 { println!("<<< {}", w); }
		self.write_len(w.len() as u32);
		self.write_str(&w.as_bytes());
	}
	pub fn write_sentence(&mut self, words: Vec<String>) -> u32{
		let mut ret: u32 = 0;
		for w in words {
			self.write_word(w);
			ret += 1;
		}
		self.write_word("".to_string());
		ret
	}
	pub fn read_sentence(&mut self) -> Vec<String>  {
		let mut r: Vec<String> = Vec::new();
		loop {
			let w = self.read_word();
			if &w[..] == "" {
				return r;
			}
			r.push(w);
		}
	}
	fn talk(&mut self, words: Vec<String>) -> Vec<(String, BTreeMap<String, String>)>{
		if self.write_sentence(words) == 0 {
			return vec![];
		}
		let mut r: Vec<(String, BTreeMap<String, String>)> = Vec::new();
		loop {
			let i: Vec<String> = self.read_sentence();
			if i.len() == 0 {
				continue;
			}
			let reply: String = i[0].clone();
			let mut attrs: BTreeMap<String, String> = BTreeMap::new();
			for w in &i[1..] {
				match w[1..].find("=") {
					Some(n) => { attrs.insert( 	w[..n+1].to_string() ,
												w[(n+2)..].to_string() ); }
					None    => { attrs.insert(w.clone(), "".to_string()); }
				};
			}
			r.push((reply.clone(), attrs));
			if reply == "!done" {
				return r;
			}
		}
	}
	pub fn login(&mut self, username: String, pwd: String) {
		let mut chal: Vec<u8> = Vec::new();
		for (_ /*reply*/, attrs) in self.talk(vec![r"/login".to_string()]) {
			chal = hex_binascii(attrs["=ret"].clone()).unwrap();
		}
		let mut md = Md5::new();
		md.input(&[0]);
		md.input(pwd.as_bytes());
		md.input(&chal[..]);
		self.talk(vec![r"/login".to_string(), format!("=name={}", username),
						format!("=response=00{}",md.result_str())]);
	}
}