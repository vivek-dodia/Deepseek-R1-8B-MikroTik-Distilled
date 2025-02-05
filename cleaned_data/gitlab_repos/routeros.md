# Repository Information
Name: routeros

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
	url = https://gitlab.com/rtician/routeros.git
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
language: python
python:
        - "2.7"
        - "3.3"
        - "3.4"
        - "3.5"
        - "3.6"
install: "pip install -r requirements.txt"
script: nosetests
================================================

File: LICENSE
================================================
MIT License
Copyright (c) 2017 Ramiro Tician
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
================================================

File: README.md
================================================
# RouterOS
[![Build Status](https://travis-ci.org/rtician/routeros.svg?branch=master)](https://travis-ci.org/rtician/routeros)
RouterOS is a API client for Mikrotik RouterOS.
### How can I install it?
```
$ pip install routeros 
```
The usage of a virtualenv is recommended.
### How to use it?
```python
In [1]: from routeros import login
In [2]: routeros = login('user', 'password', '10.1.0.1')
In [3]: routeros('/ip/pool/print')
Out[3]: 
({'.id': '*1', 'name': 'dhcp', 'ranges': '192.168.88.10-192.168.88.254'},
 {'.id': '*2', 'name': 'hs-pool-8', 'ranges': '10.5.50.2-10.5.50.254'})
In [4]: routeros.close()
In [5]: 
```
### Also can use query
Query can consult specific attributes on routeros.
**Methods:**
> - query.has(*args)
> - query.hasnot(*args)
> - query.equal(**kwargs)
> - query.lower(**kwargs)
> - query.greater(**kwargs)
```python
In [1]: from routeros import login
In [2]: routeros = login('user', 'password', '10.1.0.1')
In [3]: routeros.query('/ip/pool/print').equal(name='dhcp')
Out[3]: ({'.id': '*1', 'name': 'dhcp', 'ranges': '192.168.88.10-192.168.88.254'},)
In [4]: routeros.close()
In [5]: 
```
================================================

File: requirements.txt
================================================
Pygments==2.2.0
coverage==4.4.1
decorator==4.1.2
ipython-genutils==0.2.0
ipython==5.5.0
jedi==0.11.0
mock==2.0.0
nose==1.3.7
parso==0.1.0
pbr==3.1.1
pexpect==4.3.0
pickleshare==0.7.4
prompt-toolkit==1.0.15
ptyprocess==0.5.2
py==1.4.34
pytest==3.2.3
simplegeneric==0.8.1
six==1.11.0
traitlets==4.3.2
wcwidth==0.1.7
================================================

File: api.py
================================================
from routeros.exc import TrapError
class Parser:
    @staticmethod
    def parse_word(word):
        """
        Split given attribute word to key, value pair.
        Values are casted to python equivalents.
        :param word: API word.
        :returns: Key, value pair.
        """
        _, key, value = word.split('=', 2)
        return key, value
    @staticmethod
    def compose_word(key, value):
        '''
        Create a attribute word from key, value pair.
        Values are casted to api equivalents.
        '''
        return '={0}={1}'.format(key, value)
class Query:
    def __init__(self, api, command):
        self.api = api
        self.command = command
    def has(self, *args):
        words = ['?{0}'.format(arg) for arg in args]
        return self.api(self.command, *words)
    def hasnot(self, *args):
        words = ['?-{0}'.format(arg) for arg in args]
        return self.api(self.command, *words)
    def equal(self, **kwargs):
        words = ['?={0}={1}'.format(key, value) for key, value in kwargs.items()]
        return self.api(self.command, *words)
    def lower(self, **kwargs):
        words = ['?<{0}={1}'.format(key, value) for key, value in kwargs.items()]
        return self.api(self.command, *words)
    def greater(self, **kwargs):
        words = ['?>{0}={1}'.format(key, value) for key, value in kwargs.items()]
        return self.api(self.command, *words)
class RouterOS(Parser):
    def __init__(self, protocol):
        self.protocol = protocol
    def __call__(self, command, *args, **kwargs):
        """
        Call Api with given command.
        :param command: Command word. eg. /ip/address/print
        :param args: List with optional arguments, most used for query commands.
        :param kwargs: Dictionary with optional arguments.
        """
        if kwargs:
            args = tuple(self.compose_word(key, value) for key, value in kwargs.items())
        self.protocol.write_sentence(command, *args)
        return self._read_response()
    def query(self, command):
        return Query(self, command)
    def _read_sentence(self):
        """
        Read one sentence and parse words.
        :returns: Reply word, dict with attribute words.
        """
        reply_word, words = self.protocol.read_sentence()
        words = dict(self.parse_word(word) for word in words)
        return reply_word, words
    def _read_response(self):
        """
        Read until !done is received.
        :throws TrapError: If one !trap is received.
        :returns: Full response
        """
        response = []
        reply_word = None
        while reply_word != '!done':
            reply_word, words = self._read_sentence()
            response.append((reply_word, words))
        if '!trap' in response:
            raise TrapError()
        # Remove empty sentences
        return tuple(words for reply_word, words in response if words)
    def close(self):
        self.protocol.close()
================================================

File: exc.py
================================================
class TrapError(Exception):
    """
    Exception raised when !trap is received!
    """
    pass
class FatalError(Exception):
    """
    Exception raised when !fatal is received!
    """
    pass
class ConnectionError(Exception):
    """
    Exception raised when is not possible to connect to routerOS!
    """
    pass
================================================

File: utils.py
================================================
from socket import SHUT_RDWR, error as SOCKET_ERROR, timeout as SOCKET_TIMEOUT
from struct import pack, unpack
from routeros.exc import ConnectionError, FatalError
class Socket:
    def __init__(self, sock):
        self.sock = sock
    def write(self, string):
        """
        Write given bytes string to socket. Loop as long as every byte in
        string is written unless exception is raised.
        :param string: string to write on socket.
        """
        try:
            self.sock.sendall(string)
        except SOCKET_TIMEOUT as exc:
            raise ConnectionError('Socket timed out. ' + str(exc))
        except SOCKET_ERROR as exc:
            raise ConnectionError('Failed to write to socket. ' + str(exc))
    def read(self, length):
        """
        Read as many bytes from socket as specified in length.
        Loop as long as every byte is read unless exception is raised.
        :param length: length to read on socket.
        :return: data (string) received from socket.
        """
        try:
            data = self.sock.recv(length)
            if not data:
                raise ConnectionError('Connection was closed.')
            return data
        except SOCKET_TIMEOUT as exc:
            raise ConnectionError('Socket timed out. ' + str(exc))
        except SOCKET_ERROR as exc:
            raise ConnectionError('Failed to read from socket. {0}'.format(exc))
    def close(self):
        """
        Close connection with the socket.
        """
        try:
            # inform other end that we will not read and write any more
            self.sock.shutdown(SHUT_RDWR)
        except SOCKET_ERROR:
            pass
        finally:
            self.sock.close()
class APIUtils:
    @staticmethod
    def encode_length(length):
        """
        Decode length based on given bytes.
        :param length: bytes string to decode.
        :return: decoded length.
        """
        if length < 0x80:
            new_length = length
            offset = -1
        elif length < 0x4000:
            new_length = length | 0x8000
            offset = -2
        elif length < 0x200000:
            new_length = length | 0xC00000
            offset = -3
        elif length < 0x10000000:
            new_length = length | 0xE0000000
            offset = -4
        else:
            raise ConnectionError('Unable to encode length of {}'.format(length))
        return pack('!I', new_length)[offset:]
    def encode_word(self, encoding, word):
        """
        Encode word in API format.
        :param word: Word to encode.
        :param encoding: encoding type.
        :return: encoded word.
        """
        encoded_word = word.encode(encoding=encoding, errors='strict')
        return self.encode_length(len(word)) + encoded_word
    def encode_sentence(self, encoding, *words):
        """
        Encode given sentence in API format.
        :param words: Words to encode.
        :param encoding: encoding type.
        :returns: Encoded sentence.
        """
        encoded = [self.encode_word(encoding, word) for word in words]
        encoded = b''.join(encoded)
        # append EOS (end of sentence) byte
        encoded += b'\x00'
        return encoded
    @staticmethod
    def decode_bytes(bytes):
        """
        Decode length based on given bytes.
        :param bytes: bytes string to decode.
        :return: decoded length.
        """
        length = len(bytes)
        if length < 2:
            offset = b'\x00\x00\x00'
            xor = 0
        elif length < 3:
            offset = b'\x00\x00'
            xor = 0x8000
        elif length < 4:
            offset = b'\x00'
            xor = 0xC00000
        elif length < 5:
            offset = b''
            xor = 0xE0000000
        else:
            raise ConnectionError('Unable to decode length of {}'.format(length))
        decoded = unpack('!I', (offset + bytes))[0]
        decoded ^= xor
        return decoded
    @staticmethod
    def determine_length(length):
        """
        Given first read byte, determine how many more bytes
        needs to be known in order to get fully encoded length.
        :param length: first read byte.
        :return: how many bytes to read.
        """
        integer = ord(length)
        if integer < 128:
            return 0
        elif integer < 192:
            return 1
        elif integer < 224:
            return 2
        elif integer < 240:
            return 3
        else:
            raise ConnectionError('Unknown controll byte {}'.format(length))
    def decode_sentence(self, encoding, sentence):
        """
        Decode given sentence.
        :param encoding: encoding type.
        :param sentence: bytes string with sentence (without ending \x00 EOS byte).
        :return: tuple with decoded words.
        """
        words = []
        start, end = 0, 1
        while end < len(sentence):
            end += self.determine_length(sentence[start:end])
            word_length = self.decode_bytes(sentence[start:end])
            words.append(sentence[end:word_length+end])
            start, end = end + word_length, end + word_length + 1
        return tuple(word.decode(encoding=encoding, errors='strict') for word in words)
class API(APIUtils):
    def __init__(self, transport, encoding):
        self.transport = transport
        self.encoding = encoding
    def write_sentence(self, command, *words):
        """
        Write encoded sentence.
        :param command: Command word.
        :param words: Parameter words.
        """
        encoded = self.encode_sentence(self.encoding, command, *words)
        self.transport.write(encoded)
    def read_sentence(self):
        """
        Read every word until empty word (NULL byte) is received.
        :return: Reply word, tuple with read words.
        """
        sentence = tuple(word for word in iter(self.read_word, None))
        reply_word, words = sentence[0], sentence[1:]
        if reply_word == '!fatal':
            self.transport.close()
            raise FatalError(words[0])
        else:
            return reply_word, words
    def read_word(self):
        bytes = self.transport.read(1)
        read = self.determine_length(bytes)
        if read:
            bytes += self.transport.read(read)
        bytes = self.decode_bytes(bytes)
        if not bytes:
            return
        return self.transport.read(bytes).decode(encoding=self.encoding, errors='strict')
    def close(self):
        self.transport.close()
================================================

File: __init__.py
================================================
# -*- coding: UTF-8 -*-
from socket import create_connection, error as SOCKET_ERROR, timeout as SOCKET_TIMEOUT
from binascii import unhexlify, hexlify
from hashlib import md5
from routeros.exc import TrapError, FatalError, ConnectionError
from routeros.utils import API, Socket
from routeros.api import RouterOS
def login(username, password, host, port=8728):
    """
    Connect and login to routeros device.
    Upon success return a RouterOS class.
    :param username: Username to login with.
    :param password: Password to login with. Only ASCII characters allowed.
    :param host: Hostname to connect to. May be ipv4,ipv6, FQDN.
    :param port: Destination port to be used. Defaults to 8728.
    """
    transport = create_transport(host, port)
    protocol = API(transport=transport, encoding='ASCII')
    routeros = RouterOS(protocol=protocol)
    try:
        sentence = routeros('/login')
        token = sentence[0]['ret']
        encoded = encode_password(token, password)
        routeros('/login', **{'name': username, 'response': encoded})
    except (ConnectionError, TrapError, FatalError):
        transport.close()
        raise
    return routeros
def create_transport(host, port):
    """
    Create a connection with host and return a open Socket
    :param host: Hostname to connect to. May be ipv4,ipv6, FQDN.
    :param port: Destination port to be used.
    :return: Socket.
    """
    try:
        sock = create_connection(address=(host, port), timeout=10)
    except (SOCKET_ERROR, SOCKET_TIMEOUT) as error:
        raise ConnectionError(error)
    return Socket(sock=sock)
def encode_password(token, password):
    """
    Encode a password token receive from routeros login attempt.
    :param token: token returned from routeros.
    :param password: password to login with. Only ASCII characters allowed.
    :return: A valid password to connect on routeros. 
    """
    token = token.encode('ascii', 'strict')
    token = unhexlify(token)
    password = password.encode('ascii', 'strict')
    md = md5()
    md.update(b'\x00' + password + token)
    password = hexlify(md.digest())
    return '00' + password.decode('ascii', 'strict')
================================================

File: setup.py
================================================
from distutils.core import setup
setup(
  name='routeros',
  packages=['routeros'],
  version='1.1',
  description='Implementation of Mikrotik API',
  license='MIT',
  author='Ramiro Tician',
  author_email='ramirotician@gmail.com',
  url='https://github.com/rtician/routeros',
  download_url='https://github.com/rtician/routeros/archive/v1.1.tar.gz',
  keywords=['mikrotik', 'routeros', 'api'],
  classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'Operating System :: MacOS',
      'Operating System :: Microsoft :: Windows',
      'Operating System :: Unix',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Topic :: Software Development :: Libraries'
  ],
)
================================================

File: test_api.py
================================================
import unittest
from routeros.api import Query, Parser
class MockedAPI:
    def __call__(self, command, *words):
        return [command] + [word for word in words]
class TestQuery(unittest.TestCase):
    def setUp(self):
        self.api = MockedAPI()
        self.command = '/ip/pool/print'
        self.query = Query(self.api, self.command)
    def test_query(self):
        # We don't need the attributes in order.
        expected_equal = sorted([self.command, '?=foo=bar', '?=bar=foo'])
        self.assertEqual(self.query.equal(foo='bar', bar='foo')[0], self.command)
        self.assertEqual(sorted(self.query.equal(foo='bar', bar='foo')), expected_equal)
        expected_has = sorted([self.command, '?foo', '?bar'])
        self.assertEqual(self.query.equal(foo='bar', bar='foo')[0], self.command)
        self.assertEqual(sorted(self.query.has('foo', 'bar')), expected_has)
        expected_hasnot = sorted([self.command, '?-foo', '?-bar'])
        self.assertEqual(self.query.equal(foo='bar', bar='foo')[0], self.command)
        self.assertEqual(sorted(self.query.hasnot('foo', 'bar')), expected_hasnot)
        expected_lower = sorted([self.command, '?<foo=bar', '?<bar=foo'])
        self.assertEqual(self.query.equal(foo='bar', bar='foo')[0], self.command)
        self.assertEqual(sorted(self.query.lower(foo='bar', bar='foo')), expected_lower)
        expected_greater = sorted([self.command, '?>foo=bar', '?>bar=foo'])
        self.assertEqual(self.query.equal(foo='bar', bar='foo')[0], self.command)
        self.assertEqual(sorted(self.query.greater(foo='bar', bar='foo')), expected_greater)
class TestParser(unittest.TestCase):
    def setUp(self):
        self.attributes = (
            {
                'attr': '=.id=value',
                'key': '.id',
                'value': 'value',
            },
            {
                'attr': '=name=ether1',
                'key': 'name',
                'value': 'ether1',
            },
            {
                'attr': '=comment=',
                'key': 'comment',
                'value': '',
            }
        )
    def test_parse_word(self):
        for attribute in self.attributes:
            self.assertEqual(Parser.parse_word(attribute['attr']),
                             (attribute['key'], attribute['value']))
    def test_compose_word(self):
        for attribute in self.attributes:
            attr = Parser.compose_word(attribute['key'], attribute['value'])
            self.assertEqual(attribute['attr'], attr)
================================================

File: test_login.py
================================================
import unittest
from mock import patch
from socket import error as SOCKET_ERROR, timeout as SOCKET_TIMEOUT
from routeros import encode_password, create_transport, ConnectionError
class TestLogin(unittest.TestCase):
    def test_password_encoding(self):
        expected_value = '00c7fd865183a43a772dde231f6d0bff13'
        self.assertEqual(encode_password('259e0bc05acd6f46926dc2f809ed1bba', 'test'),
                         expected_value)
    def test_non_ascii_password_encoding(self):
        # Only ascii characters are allowed in password.
        with self.assertRaises(UnicodeEncodeError):
            encode_password(
                token='259e0bc05acd6f46926dc2f809ed1bba',
                password=b'\xc5\x82\xc4\x85'.decode('utf-8')
            )
    def test_create_transport_calls_create_connection(self):
        with patch('routeros.create_connection') as connection:
            create_transport(host='127.0.0.1', port=9099)
            connection.assert_called_once_with(address=('127.0.0.1', 9099), timeout=10)
    def test_create_transport_raises_connection_error(self):
        for error in (SOCKET_ERROR, SOCKET_TIMEOUT):
            with patch('routeros.create_connection') as connection:
                connection.side_effect = error
                with self.assertRaises(ConnectionError):
                    create_transport(host='127.0.0.1', port=9099)
    def test_create_transport_calls_socket(self):
        with patch('routeros.Socket') as socket:
            with patch('routeros.create_connection') as connection:
                a = create_transport(host='127.0.0.1', port=9099)
                socket.assert_called_once_with(sock=connection.return_value)
================================================

File: test_utils.py
================================================
import unittest
from mock import Mock, patch
from collections import namedtuple
from struct import pack
from socket import SHUT_RDWR, error as SOCKET_ERROR
from routeros.utils import Socket, API, APIUtils
from routeros.exc import ConnectionError, FatalError
class TestSocket(unittest.TestCase):
    def setUp(self):
        self.transport = Socket(sock=Mock(sock='socket'))
    def test_calls_sendall(self):
        self.transport.write(b'foo bar')
        self.transport.sock.sendall.assert_called_once_with(b'foo bar')
    def test_calls_shutdown(self):
        self.transport.close()
        self.transport.sock.shutdown.assert_called_once_with(SHUT_RDWR)
    def test_close_shutdown_exception(self):
        self.transport.sock.shutdown.side_effect = SOCKET_ERROR
        self.transport.close()
        self.transport.sock.close.assert_called_once_with()
    def test_close(self):
        self.transport.close()
        self.transport.sock.close.assert_called_once_with()
    def test_write_raises_socket_errors(self):
        self.transport.sock.sendall.side_effect = SOCKET_ERROR
        with self.assertRaises(ConnectionError):
            self.transport.write(b'foo bar')
    def test_read_raises_when_recv_returns_empty_byte_string(self):
        self.transport.sock.recv.return_value = b''
        for length in (0, 3):
            with self.assertRaises(ConnectionError):
                self.transport.read(length)
    def test_read_returns_from_recv(self):
        self.transport.sock.recv.return_value = b'bar foo'
        assert self.transport.read(1024) == b'bar foo'
    def test_recv_raises_socket_errors(self):
        self.transport.sock.recv.side_effect = SOCKET_ERROR
        with self.assertRaises(ConnectionError):
            self.transport.read(2)
class TestLengthUtils(unittest.TestCase):
    def setUp(self):
        self.encoder = APIUtils.encode_length
        self.decoder = APIUtils.decode_bytes
        self.determine_length = APIUtils.determine_length
        lengths = namedtuple('lengths', ('integer', 'encoded'))
        self.valid_lengths = [
            lengths(integer=0, encoded=b'\x00'),
            lengths(integer=127, encoded=b'\x7f'),
            lengths(integer=130, encoded=b'\x80\x82'),
            lengths(integer=2097140, encoded=b'\xdf\xff\xf4'),
            lengths(integer=268435440, encoded=b'\xef\xff\xff\xf0'),
        ]
    def test_encode_length(self):
        for valid_length in self.valid_lengths:
            result = self.encoder(valid_length.integer)
            self.assertEqual(result, valid_length.encoded)
    def test_encode_length_raises_if_lenghth_is_too_big(self):
        # length must be < 268435456
        invalid_length = 268435456
        with self.assertRaises(ConnectionError):
            self.encoder(invalid_length)
    def test_decode_length(self):
        for valid_length in self.valid_lengths:
            result = self.decoder(valid_length.encoded)
            self.assertEqual(result, valid_length.integer)
    def test_decode_length_raises(self):
        # len(length) must be < 5
        invalid_bytes = b'\xff\xff\xff\xff\xff'
        with self.assertRaises(ConnectionError):
            self.decoder(invalid_bytes)
    def test_determine_length(self):
        bytes = [
            (b'x', 0),  # 120
            (b'\xbf', 1),  # 191
            (b'\xdf', 2),  # 223
            (b'\xef', 3),  # 239
        ]
        for length, expected in bytes:
            self.assertEqual(self.determine_length(length), expected)
    def test_determine_length_raises(self):
        # First byte of length must be < 240.
        invalid_lengths = (pack('>B', i) for i in range(240, 256))
        for invalid_length in invalid_lengths:
            with self.assertRaises(ConnectionError):
                self.determine_length(invalid_length)
class TestWordUtils(unittest.TestCase):
    def setUp(self):
        self.encoder = APIUtils().encode_word
    def test_encode_word(self):
        with patch('routeros.utils.APIUtils.encode_length', return_value=b'len_') as encoder:
            self.assertEqual(self.encoder('ASCII', 'word'), b'len_word')
            self.assertEqual(encoder.call_count, 1)
    def test_non_ASCII_word_encoding(self):
        # Word may only contain ASCII characters.
        word = b'\xc5\x82\xc4\x85'.decode('utf-8')
        with self.assertRaises(UnicodeEncodeError):
            self.encoder('ASCII', word)
class TestSentenceUtils(unittest.TestCase):
    def setUp(self):
        self.encoder = APIUtils().encode_sentence
        self.decoder = APIUtils().decode_sentence
    def test_encode_sentence(self):
        with patch('routeros.utils.APIUtils.encode_word', return_value=b'') as encoder:
            encoded = self.encoder('ASCII', 'first', 'second')
            self.assertEqual(encoder.call_count, 2)
            self.assertEqual(encoded[-1:], b'\x00')
    def test_decode_sentence(self):
        sentence = b'\x11/ip/address/print\x05first\x06second'
        expected = ('/ip/address/print', 'first', 'second')
        self.assertEqual(self.decoder('ASCII', sentence), expected)
    def test_decode_sentence_non_ASCII(self):
        # Word may only contain ASCII characters.
        sentence = b'\x12/ip/addres\xc5\x82/print\x05first\x06second'
        with self.assertRaises(UnicodeDecodeError):
            self.decoder('ASCII', sentence)
class TestAPI(unittest.TestCase):
    def setUp(self):
        self.api = API(transport=Mock(spec=Socket), encoding='ASCII')
    def test_write_sentence_calls_encode_sentence(self):
        with patch('routeros.utils.APIUtils.encode_sentence') as encoder:
            self.api.write_sentence('/ip/address/print', '=key=value')
            encoder.assert_called_once_with('ASCII', '/ip/address/print', '=key=value')
    def test_write_sentence_calls_transport_write(self):
        # Assert that write is called with encoded sentence.
        with patch('routeros.utils.APIUtils.encode_sentence') as encoder:
            self.api.write_sentence('/ip/address/print', '=key=value')
            self.api.transport.write.assert_called_once_with(encoder.return_value)
    def test_readSentence_raises_FatalError(self):
        # Assert that FatalError is raised with its reason.
        with patch('routeros.utils.iter', return_value=('!fatal', 'reason')):
            with self.assertRaises(FatalError):
                self.api.read_sentence()
            self.assertEqual(self.api.transport.close.call_count, 1)
    def test_close(self):
        self.api.close()
        self.api.transport.close.assert_called_once_with()