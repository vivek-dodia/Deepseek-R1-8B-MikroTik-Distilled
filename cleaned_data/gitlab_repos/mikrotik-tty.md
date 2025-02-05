# Repository Information
Name: mikrotik-tty

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
	url = https://gitlab.com/sma11case/mikrotik-tty.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: git_commit.sh
================================================
#!/bin/bash
cd "$(dirname "$0")"
SCRIPT_DIR=`pwd`
echo "WorkDir: ${SCRIPT_DIR}"
git add -A 'src/*'
git add -Af 'ROSTTY.xcodeproj/xcshareddata/*'
TODAY=`date '+%Y-%m-%d %H:%M:%S'`
if [ -n "$1" ]; then
	TODAY="$1"
fi
git commit -am "${TODAY}"
git push origin --all
git push origin --tags
exit 0
================================================

File: README.md
================================================
## Mikroti tty shell
### a simple tty for mikrotik, support OpenWrt.
### Usage:
```
mikrotik-tty [-f<commands_file>] [-u<username>] [-p<password>] [-P<portNum>] [--quiet] <ip_address>
-u<username> the username to login as.  Default is admin
-p<password> the password to use for login.  Default is empty string
-f<commands_file> the commands send to api.  Default is not use(from stdid only)
-P<port> TCP port to use for API connection.  Default is 8728.
--quiet Suppress all non-API output.  Default is interactive mode.
<ip_address> IP address to connect to.  REQUIRED
```
### Description:
* Source from [Mikrotik Wiki](https://wiki.mikrotik.com/wiki/API_in_C#Sample_Client_.28mikrotik-tty.c.29).
* Add commands file support.
* Add openwrt support.
### Sample Commands File:
**Must Keep Empty Lines! It Means Commit Commands to ROS**
```
/ip/address/print
?interface=pppoe-out1
/ip/address/print
?interface=pppoe-out2
/ip/address/print
?interface=pppoe-out3
/ip/address/print
?interface=pppoe-out4
```
### License:
* Same as [Mikrotik Wiki](https://wiki.mikrotik.com/wiki/API_in_C#Sample_Client_.28mikrotik-tty.c.29).
================================================

File: CMakeLists.txt
================================================
cmake_minimum_required(VERSION 2.6)
PROJECT(rostty)
SET(SOURCES	md5.c mikrotik-api.c mikrotik-tty.c)
ADD_EXECUTABLE(rostty ${SOURCES})
INSTALL(TARGETS rostty RUNTIME DESTINATION bin)
================================================

File: mikrotik-api.c
================================================
/********************************************************************
 * Some definitions
 * Word = piece of API code
 * Sentence = multiple words
 * Block = multiple sentences (usually in response to a sentence request)
 * 
	int fdSock;
	int iLoginResult;
	struct Sentence stSentence;
	struct Block stBlock;
	fdSock = apiConnect("10.0.0.1", 8728);
	// attempt login
	iLoginResult = ros_login(fdSock, "admin", "adminPassword");
	if (!iLoginResult)
	{
		apiDisconnect(fdSock);
		printf("Invalid username or password.\n");
		exit(1);
	}
	// initialize, fill and send sentence to the API
	initializeSentence(&stSentence);
	addWordToSentence(&stSentence, "/interface/getall");
	writeSentence(fdSock, &stSentence);
	// receive and print block from the API
	stBlock = readBlock(fdSock);
	printBlock(&stBlock);
	apiDisconnect(fdSock);
 ********************************************************************/
#include<stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<string.h>
#include<stdlib.h>
#include "md5.h"
#include "mikrotik-api.h"
int iLittleEndian;
/********************************************************************
 * Connect to API
 * Returns a socket descriptor
 ********************************************************************/
int apiConnect(char *szIPaddr, int iPort)
{
	int fdSock;
	struct sockaddr_in address;
	int iConnectResult;
	int iLen;
	fdSock = socket(AF_INET, SOCK_STREAM, 0);
	address.sin_family = AF_INET;
	address.sin_addr.s_addr = inet_addr(szIPaddr);
	address.sin_port = htons(iPort);
	iLen = sizeof(address);
	DEBUG ? printf("Connecting to %s\n", szIPaddr) : 0;
	iConnectResult = connect(fdSock, (struct sockaddr *)&address, iLen);
	if(iConnectResult==-1)
	{
		perror ("Connection problem");
		exit(1);
	}
	else
	{
		DEBUG ? printf("Successfully connected to %s\n", szIPaddr) : 0;
	}
	// determine endianness of this machine
	// iLittleEndian will be set to 1 if we are
	// on a little endian machine...otherwise
	// we are assumed to be on a big endian processor
	iLittleEndian = isLittleEndian();
	return fdSock;
}
/********************************************************************
 * Disconnect from API
 * Close the API socket
 ********************************************************************/
void apiDisconnect(int fdSock)
{
	DEBUG ? printf("Closing socket\n") : 0;
	close(fdSock);
}
/********************************************************************
 * Login to the API
 * 1 is returned on successful login
 * 0 is returned on unsuccessful login
 ********************************************************************/
int ros_login(int fdSock, char *username, char *password)
{
	struct Sentence stReadSentence;
	struct Sentence stWriteSentence;
	char *szMD5Challenge;
	char *szMD5ChallengeBinary;
	char *szMD5PasswordToSend;
	char *szLoginUsernameResponseToSend;
	char *szLoginPasswordResponseToSend;
	md5_state_t state;
	md5_byte_t digest[16];
	char cNull[1] = {0};
	writeWord(fdSock, "/login");
	writeWord(fdSock, "");
	stReadSentence = readSentence(fdSock);
	DEBUG ? printSentence (&stReadSentence) : 0;
	if (stReadSentence.iReturnValue != DONE)
	{
		printf("error.\n");
		exit(0);
	}
	// extract md5 string from the challenge sentence
	szMD5Challenge = strtok(stReadSentence.szSentence[1], "=");
	szMD5Challenge = strtok(NULL, "=");
	DEBUG ? printf("MD5 of challenge = %s\n", szMD5Challenge) : 0;
	// convert szMD5Challenge to binary
	szMD5ChallengeBinary = md5ToBinary(szMD5Challenge);
	// get md5 of the password + challenge concatenation
	md5_init(&state);
	md5_append(&state, cNull, 1);
	md5_append(&state, (const md5_byte_t *)password, strlen(password));
	md5_append(&state, (const md5_byte_t *)szMD5ChallengeBinary, strlen(szMD5ChallengeBinary));
	md5_finish(&state, digest);
	// convert this digest to a string representation of the hex values
	// digest is the binary format of what we want to send
	// szMD5PasswordToSend is the "string" hex format
	szMD5PasswordToSend = md5DigestToHexString(digest);
	clearSentence(&stReadSentence);
	DEBUG ? printf("szPasswordToSend = %s\n", szMD5PasswordToSend) : 0;
	// put together the login sentence
	initializeSentence(&stWriteSentence);
	addWordToSentence(&stWriteSentence, "/login");
	addWordToSentence(&stWriteSentence, "=name=");
	addPartWordToSentence(&stWriteSentence, username);
	addWordToSentence(&stWriteSentence, "=response=00");
	addPartWordToSentence(&stWriteSentence, szMD5PasswordToSend);
	DEBUG ? printSentence(&stWriteSentence) : 0;
	writeSentence(fdSock, &stWriteSentence);
	stReadSentence = readSentence(fdSock);
	DEBUG ? printSentence (&stReadSentence) : 0;
	if (stReadSentence.iReturnValue == DONE)
	{
		clearSentence(&stReadSentence);
		return 1;
	}
	else
	{
		clearSentence(&stReadSentence);
		return 0;
	}
}
/********************************************************************
 * Encode message length and write it out to the socket
 ********************************************************************/
void writeLen(int fdSock, int iLen)
{
	char *cEncodedLength;  // encoded length to send to the api socket
	char *cLength;         // exactly what is in memory at &iLen integer
	cLength = calloc(sizeof(int), 1);
	cEncodedLength = calloc(sizeof(int), 1);
	// set cLength address to be same as iLen
	cLength = (char *)&iLen;
	DEBUG ? printf("length of word is %d\n", iLen) : 0;
	// write 1 byte
	if (iLen < 0x80)
	{
		cEncodedLength[0] = (char)iLen;
		write (fdSock, cEncodedLength, 1);
	}
	// write 2 bytes
	else if (iLen < 0x4000)
	{
		DEBUG ? printf("iLen < 0x4000.\n") : 0;
		if (iLittleEndian)
		{
			cEncodedLength[0] = cLength[1] | 0x80;
			cEncodedLength[1] = cLength[0];
		}
		else
		{
			cEncodedLength[0] = cLength[2] | 0x80;
			cEncodedLength[1] = cLength[3];
		}
		write (fdSock, cEncodedLength, 2);
	}
	// write 3 bytes
 	else if (iLen < 0x200000)
	{
		DEBUG ? printf("iLen < 0x200000.\n") : 0;
		if (iLittleEndian)
		{
			cEncodedLength[0] = cLength[2] | 0xc0;
			cEncodedLength[1] = cLength[1];
			cEncodedLength[2] = cLength[0];
		}
		else
		{
			cEncodedLength[0] = cLength[1] | 0xc0;
			cEncodedLength[1] = cLength[2];
			cEncodedLength[2] = cLength[3];
		}
		write (fdSock, cEncodedLength, 3);
	}
	// write 4 bytes
	// this code SHOULD work, but is untested...
	else if (iLen < 0x10000000)
	{
		DEBUG ? printf("iLen < 0x10000000.\n") : 0;
		if (iLittleEndian)
		{
			cEncodedLength[0] = cLength[3] | 0xe0;
			cEncodedLength[1] = cLength[2];
			cEncodedLength[2] = cLength[1];
			cEncodedLength[3] = cLength[0];
		}
		else
		{
			cEncodedLength[0] = cLength[0] | 0xe0;
			cEncodedLength[1] = cLength[1];
			cEncodedLength[2] = cLength[2];
			cEncodedLength[3] = cLength[3];
		}
		write (fdSock, cEncodedLength, 4);
	}
	else  // this should never happen
	{
		printf("length of word is %d\n", iLen);
		printf("word is too long.\n");
		exit(1);
	}
}
/********************************************************************
 * Write a word to the socket
 ********************************************************************/
void writeWord(int fdSock, char *szWord)
{
	DEBUG ? printf("Word to write is %s\n", szWord) : 0;
	writeLen(fdSock, strlen(szWord));
	write(fdSock, szWord, strlen(szWord));
}
/********************************************************************
 * Write a sentence (multiple words) to the socket
 ********************************************************************/
void writeSentence(int fdSock, struct Sentence *stWriteSentence)
{
	int iIndex;
	if (stWriteSentence->iLength == 0)
	{
		return;
	}
	DEBUG ? printf("Writing sentence\n"): 0;
	DEBUG ? printSentence(stWriteSentence) : 0;
	for (iIndex=0; iIndex<stWriteSentence->iLength; iIndex++)
	{
		writeWord(fdSock, stWriteSentence->szSentence[iIndex]);
	}
	writeWord(fdSock, "");
}
/********************************************************************
 * Read a message length from the socket
 * 
 * 80 = 10000000 (2 character encoded length)
 * C0 = 11000000 (3 character encoded length)
 * E0 = 11100000 (4 character encoded length)
 *
 * Message length is returned
 ********************************************************************/
int readLen(int fdSock)
{
	char cFirstChar; // first character read from socket
	char *cLength;   // length of next message to read...will be cast to int at the end
	int *iLen;       // calculated length of next message (Cast to int)
	cLength = calloc(sizeof(int), 1);
	DEBUG ? printf("start readLen()\n") : 0;
	read(fdSock, &cFirstChar, 1);
	DEBUG ? printf("byte1 = %#x\n", cFirstChar) : 0;
	// read 4 bytes
	// this code SHOULD work, but is untested...
	if ((cFirstChar & 0xE0) == 0xE0)
	{
		DEBUG ? printf("4-byte encoded length\n") : 0;
		if (iLittleEndian)
		{
			cLength[3] = cFirstChar;
			cLength[3] &= 0x1f;        // mask out the 1st 3 bits
			read(fdSock, &cLength[2], 1);
			read(fdSock, &cLength[1], 1);
			read(fdSock, &cLength[0], 1);
		}
		else
		{
			cLength[0] = cFirstChar;
			cLength[0] &= 0x1f;        // mask out the 1st 3 bits
			read(fdSock, &cLength[1], 1);
			read(fdSock, &cLength[2], 1);
			read(fdSock, &cLength[3], 1);
		}
		iLen = (int *)cLength;
	}
	// read 3 bytes
	else if ((cFirstChar & 0xC0) == 0xC0)
	{
		DEBUG ? printf("3-byte encoded length\n") : 0;
		if (iLittleEndian)
		{
			cLength[2] = cFirstChar;
			cLength[2] &= 0x3f;        // mask out the 1st 2 bits
			read(fdSock, &cLength[1], 1);
			read(fdSock, &cLength[0], 1);
		}
		else
		{
			cLength[1] = cFirstChar;
			cLength[1] &= 0x3f;        // mask out the 1st 2 bits
			read(fdSock, &cLength[2], 1);
			read(fdSock, &cLength[3], 1);
		}
		iLen = (int *)cLength;
	}
	// read 2 bytes
	else if ((cFirstChar & 0x80) == 0x80)
	{
		DEBUG ? printf("2-byte encoded length\n") : 0;
		if (iLittleEndian)
		{
			cLength[1] = cFirstChar;
			cLength[1] &= 0x7f;        // mask out the 1st bit
			read(fdSock, &cLength[0], 1);
		}
		else
		{
			cLength[2] = cFirstChar;
			cLength[2] &= 0x7f;        // mask out the 1st bit
			read(fdSock, &cLength[3], 1);
		}
		iLen = (int *)cLength;
	}
	// assume 1-byte encoded length...same on both LE and BE systems
	else
	{
		DEBUG ? printf("1-byte encoded length\n") : 0;
		iLen = malloc(sizeof(int));
		*iLen = (int)cFirstChar;
	}
	return *iLen;
}
/********************************************************************
 * Read a word from the socket
 * The word that was read is returned as a string
 ********************************************************************/
char *readWord(int fdSock)
{
	int iLen = readLen(fdSock);
	int iBytesToRead = 0;
	int iBytesRead = 0;
	char *szWord;
	char *szRetWord;
	char *szTmpWord;
	DEBUG ? printf("readWord iLen=%x\n", iLen) : 0;
	if (iLen > 0)
	{
		// allocate memory for strings
		szRetWord = calloc(sizeof(char), iLen + 1);
		szTmpWord = calloc(sizeof(char), 1024 + 1);
		while (iLen != 0)
		{
			// determine number of bytes to read this time around
			// lesser of 1024 or the number of byes left to read
			// in this word
			iBytesToRead = iLen > 1024 ? 1024 : iLen;
			// read iBytesToRead from the socket
			iBytesRead = read(fdSock, szTmpWord, iBytesToRead);
			// terminate szTmpWord
			szTmpWord[iBytesRead] = 0;
			// concatenate szTmpWord to szRetWord
			strcat(szRetWord, szTmpWord);
			// subtract the number of bytes we just read from iLen
			iLen -= iBytesRead;
		}		
		// deallocate szTmpWord
		free(szTmpWord);
		DEBUG ? printf("word = %s\n", szRetWord) : 0;
		return szRetWord;
	}
	else
	{
		return NULL;
	}
}
/********************************************************************
 * Read a sentence from the socket
 * A Sentence struct is returned
 ********************************************************************/
struct Sentence readSentence(int fdSock)
{
	struct Sentence stReturnSentence;
	char *szWord;
	int i=0;
	int iReturnLength=0;
	DEBUG ? printf("readSentence\n") : 0;
	initializeSentence(&stReturnSentence);
	while (szWord = readWord(fdSock))
	{
		addWordToSentence(&stReturnSentence, szWord);
		// check to see if we can get a return value from the API
		if (strstr(szWord, "!done") != NULL)
		{
			DEBUG ? printf("return sentence contains !done\n") : 0;
			stReturnSentence.iReturnValue = DONE;
		}
		else if (strstr(szWord, "!trap") != NULL)
		{
			DEBUG ? printf("return sentence contains !trap\n") : 0;
			stReturnSentence.iReturnValue = TRAP;
		}
		else if (strstr(szWord, "!fatal") != NULL)
		{
			DEBUG ? printf("return sentence contains !fatal\n") : 0;
			stReturnSentence.iReturnValue = FATAL;
		}
	}
	// if any errors, get the next sentence
	if (stReturnSentence.iReturnValue == TRAP || stReturnSentence.iReturnValue == FATAL)
	{
		readSentence(fdSock);
	}
	if (DEBUG)
	{
		for (i=0; i<stReturnSentence.iLength; i++)
		{
			printf("stReturnSentence.szSentence[%d] = %s\n", i, stReturnSentence.szSentence[i]);
		}
	}
	return stReturnSentence;
}
/********************************************************************
 * Read sentence block from the socket...keeps reading sentences
 * until it encounters !done, !trap or !fatal from the socket
 ********************************************************************/
struct Block readBlock(int fdSock)
{
	struct Sentence stSentence;
    struct Block stBlock;
	initializeBlock(&stBlock);
	DEBUG ? printf("readBlock\n") : 0;
	do
	{
		stSentence = readSentence(fdSock);
		DEBUG ? printf("readSentence succeeded.\n") : 0;
		addSentenceToBlock(&stBlock, &stSentence);
		DEBUG ? printf("addSentenceToBlock succeeded\n") : 0;
	} while (stSentence.iReturnValue == 0);
	DEBUG ? printf("readBlock completed successfully\n") : 0;
	return stBlock;
}
/********************************************************************
 * Initialize a new block
 * Set iLength to 0.
 ********************************************************************/
void initializeBlock(struct Block *stBlock)
{
	DEBUG ? printf("initializeBlock\n") : 0;
	stBlock->iLength = 0;
}
/********************************************************************
 * Clear an existing block
 * Free all sentences in the Block struct and set iLength to 0.
 ********************************************************************/
void clearBlock(struct Block *stBlock)
{
	DEBUG ? printf("clearBlock\n") : 0;
	free(stBlock->stSentence);
	initializeBlock(stBlock);
}
/********************************************************************
 * Print a block.
 * Output a Block with printf.
 ********************************************************************/
void printBlock(struct Block *stBlock)
{
	int i;
	DEBUG ? printf("printBlock\n") : 0;
	DEBUG ? printf("block iLength = %d\n", stBlock->iLength) : 0;
	for (i=0; i<stBlock->iLength; i++)
	{
		printSentence(stBlock->stSentence[i]);
	}
}
/********************************************************************
 * Add a sentence to a block
 * Allocate memory and add a sentence to a Block.
 ********************************************************************/
void addSentenceToBlock(struct Block *stBlock, struct Sentence *stSentence)
{
	int iNewLength;
	iNewLength = stBlock->iLength + 1;
	DEBUG ? printf("addSentenceToBlock iNewLength=%d\n", iNewLength) : 0;
	// allocate mem for the new Sentence position
	if (stBlock->iLength == 0)
	{
		stBlock->stSentence = malloc(1 * sizeof stBlock->stSentence);
	}
	else
	{
		stBlock->stSentence = realloc(stBlock->stSentence, iNewLength * sizeof stBlock->stSentence + 1);
	}
	// allocate mem for the full sentence struct
	stBlock->stSentence[stBlock->iLength] = malloc(sizeof *stSentence);
	// copy actual sentence struct to the block position
	memcpy(stBlock->stSentence[stBlock->iLength], stSentence, sizeof *stSentence);
	// update iLength
	stBlock->iLength = iNewLength;
	DEBUG ? printf("addSentenceToBlock stBlock->iLength=%d\n", stBlock->iLength) : 0;
}
/********************************************************************
 * Initialize a new sentence
 ********************************************************************/
void initializeSentence(struct Sentence *stSentence)
{
	DEBUG ? printf("initializeSentence\n") : 0;
	stSentence->iLength = 0;
	stSentence->iReturnValue = 0;
}
/********************************************************************
 * Clear an existing sentence
 ********************************************************************/
void clearSentence(struct Sentence *stSentence)
{
	DEBUG ? printf("initializeSentence\n") : 0;
	free(stSentence->szSentence);
	initializeSentence(stSentence);
}
/********************************************************************
 * Add a word to a sentence struct
 ********************************************************************/
void addWordToSentence(struct Sentence *stSentence, char *szWordToAdd)
{
	int iNewLength;
	iNewLength = stSentence->iLength + 1;
	// allocate mem for the new word position
	if (stSentence->iLength == 0)
	{
		stSentence->szSentence = malloc(1 * sizeof stSentence->szSentence);
	}
	else
	{
		stSentence->szSentence = realloc(stSentence->szSentence, iNewLength * sizeof stSentence->szSentence + 1);
	}
	// allocate mem for the full word string
	stSentence->szSentence[stSentence->iLength] = malloc(strlen(szWordToAdd) + 1);
	// copy word string to the sentence
	strcpy(stSentence->szSentence[stSentence->iLength], szWordToAdd);
	// update iLength
	stSentence->iLength = iNewLength;
}
/********************************************************************
 * Add a partial word to a sentence struct...useful for concatenation
 ********************************************************************/
void addPartWordToSentence(struct Sentence *stSentence, char *szWordToAdd)
{
	int iIndex;
	iIndex = stSentence->iLength - 1;
	// reallocate memory for the new partial word
	stSentence->szSentence[iIndex] = realloc(stSentence->szSentence[iIndex], strlen(stSentence->szSentence[iIndex]) + strlen(szWordToAdd) + 1);
	// concatenate the partial word to the existing sentence
	strcat (stSentence->szSentence[iIndex], szWordToAdd);
}
/********************************************************************
 * Print a Sentence struct
 ********************************************************************/
void printSentence(struct Sentence *stSentence)
{
	int i;
	DEBUG ? printf("Sentence iLength = %d\n", stSentence->iLength) : 0;
	DEBUG ? printf("Sentence iReturnValue = %d\n", stSentence->iReturnValue) : 0;
	printf("Sentence iLength = %d\n", stSentence->iLength);
	printf("Sentence iReturnValue = %d\n", stSentence->iReturnValue);
	for (i=0; i<stSentence->iLength; i++)
	{
		printf(">>> %s\n", stSentence->szSentence[i]);
	}
	printf("\n");
}
/********************************************************************
 * MD5 helper function to convert an md5 hex char representation to
 * binary representation.
 ********************************************************************/
char *md5ToBinary(char *szHex)
{
	int di;
	char cBinWork[3];
	char *szReturn;
	// allocate 16 + 1 bytes for our return string
	szReturn = malloc((16 + 1) * sizeof *szReturn);
	// 32 bytes in szHex?
	if (strlen(szHex) != 32)
	{
		return NULL;
	}
	for (di=0; di<32; di+=2)
	{
		cBinWork[0] = szHex[di];
		cBinWork[1] = szHex[di + 1];
		cBinWork[2] = 0;
		DEBUG ? printf("cBinWork = %s\n", cBinWork) : 0;
		szReturn[di/2] = hexStringToChar(cBinWork);
	}
	return szReturn;
}
/********************************************************************
 * MD5 helper function to calculate and return hex representation
 * of an MD5 digest stored in binary.
 ********************************************************************/
char *md5DigestToHexString(md5_byte_t *binaryDigest)
{
	int di;
	char *szReturn;
	// allocate 32 + 1 bytes for our return string
	szReturn = malloc((32 + 1) * sizeof *szReturn);
	for (di = 0; di < 16; ++di)
	{
		sprintf(szReturn + di * 2, "%02x", binaryDigest[di]);
	}
	return szReturn;
}
/********************************************************************
 * Quick and dirty function to convert hex string to char...
 * the toConvert string MUST BE 2 characters + null terminated.
 ********************************************************************/
char hexStringToChar(char *cToConvert)
{
	char cConverted;
	unsigned int iAccumulated=0;
	char cString0[2] = {cToConvert[0], 0};
	char cString1[2] = {cToConvert[1], 0};
	// look @ first char in the 16^1 place
	if (cToConvert[0] == 'f' || cToConvert[0] == 'F')
	{
		iAccumulated += 16*15;
	}
	else if (cToConvert[0] == 'e' || cToConvert[0] == 'E')
	{
		iAccumulated += 16*14;
	}
	else if (cToConvert[0] == 'd' || cToConvert[0] == 'D')
	{
		iAccumulated += 16*13;
	}
	else if (cToConvert[0] == 'c' || cToConvert[0] == 'C')
	{
		iAccumulated += 16*12;
	}
	else if (cToConvert[0] == 'b' || cToConvert[0] == 'B')
	{
		iAccumulated += 16*11;
	}
	else if (cToConvert[0] == 'a' || cToConvert[0] == 'A')
	{
		iAccumulated += 16*10;
	}
	else
	{
		iAccumulated += 16 * atoi(cString0);
	}
	// now look @ the second car in the 16^0 place
	if (cToConvert[1] == 'f' || cToConvert[1] == 'F')
	{
		iAccumulated += 15;
	}
	else if (cToConvert[1] == 'e' || cToConvert[1] == 'E')
	{
		iAccumulated += 14;
	}
	else if (cToConvert[1] == 'd' || cToConvert[1] == 'D')
	{
		iAccumulated += 13;
	}
	else if (cToConvert[1] == 'c' || cToConvert[1] == 'C')
	{
		iAccumulated += 12;
	}
	else if (cToConvert[1] == 'b' || cToConvert[1] == 'B')
	{
		iAccumulated += 11;
	}
	else if (cToConvert[1] == 'a' || cToConvert[1] == 'A')
	{
		iAccumulated += 10;
	}
	else
	{
		iAccumulated += atoi(cString1);
	}
	DEBUG ? printf("%d\n", iAccumulated) : 0;
	return (char)iAccumulated;	
}
/********************************************************************
 * Test whether or not this system is little endian at RUNTIME
 * Courtesy: http://download.osgeo.org/grass/grass6_progman/endian_8c_source.html
 ********************************************************************/
int isLittleEndian(void)
{
	union
	{
		int testWord;
		char testByte[sizeof(int)];
	} endianTest;
	endianTest.testWord = 1;
	if (endianTest.testByte[0] == 1)
	return 1;               /* true: little endian */
	return 0;                   /* false: big endian */
}
================================================

File: mikrotik-api.h
================================================
#include "md5.h"
#ifndef DEBUG
#define DEBUG 0
#endif
#define DONE 1
#define TRAP 2
#define FATAL 3
struct Sentence {
	char **szSentence;    // array of strings representing individual words
	int iLength;          // length of szSentence (number of array elements)
	int iReturnValue;     // return value of sentence reads from API
};
struct Block {
	struct Sentence **stSentence;
	int iLength;
};
// endianness variable...global
extern int iLittleEndian;
// API specific functions
int apiConnect(char *, int);
void apiDisconnect(int);
int ros_login(int, char *, char *);
void writeLen(int, int);
int readLen(int);
void writeWord(int, char *);
char *readWord(int);
// API helper functions to make things a little bit easier
void initializeSentence(struct Sentence *);
void clearSentence(struct Sentence *);
void writeSentence(int, struct Sentence *);
struct Sentence readSentence(int);
void printSentence(struct Sentence *);
void addWordToSentence(struct Sentence *, char *);
void addPartWordToSentence(struct Sentence *, char *);
void initializeBlock(struct Block *);
void clearBlock(struct Block *);
struct Block readBlock(int);
void addSentenceToBlock(struct Block *, struct Sentence *);
void printBlock(struct Block *);
// MD5 helper functions
char *md5DigestToHexString(md5_byte_t *);
char *md5ToBinary(char *);
char hexStringToChar(char *);
// Endian tests
int isLittleEndian(void);
================================================

File: mikrotik-tty.c
================================================
#include<stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<string.h>
#include<stdlib.h>
#include "mikrotik-api.h"
#define clog(...)
//#define clog(...) printf(__VA_ARGS__)
/********************************************************************
 * Print program usage
 ********************************************************************/
void usage()
{
	printf("Usage: mikrotik-tty [-f<commands_file>] [-u<username>] [-p<password>] [-P<portNum>] [--quiet] <ip_address>\n\n");
	printf("-u<username> the username to login as.  Default is admin\n");
    printf("-p<password> the password to use for login.  Default is empty string\n");
    printf("-f<commands_file> the commands send to api.  Default is not use(from stdid only)\n");
	printf("-P<port> TCP port to use for API connection.  Default is 8728.\n");
	printf("--quiet Suppress all non-API output.  Default is interactive mode.\n");
	printf("<ip_address> IP address to connect to.  REQUIRED\n\n");
}
/********************************************************************
 * main
 ********************************************************************/
int main(int argc, char *argv[])
{
	// declare variables
	int fdSock;
	char *szIPaddr;
	char *szPort = "8728"; // default port string
	int iPort;             // default port int
    char *szInputFile = NULL;  // default commands file
    char *szUsername = "admin";  // default username
	char *szPassword = "";       // default password
	int iInteractiveMode = 1;    // interactive mode...if set to 0, will supress all non-API output
	int iLoginResult;
	int iIndex;
	char cWordInput[256];        // limit user word input to 256 chars
	char *szNewline;             // used for word input from the user
	struct Sentence stSentence;
	struct Block stBlock;
	// check number of args.  if not correct, call usage and exit
	if (argc < 2)
	{
		usage();
		exit(0);
	}
	// parse command line parameters
	else
	{
		for (iIndex=0; iIndex<argc; iIndex++)
		{
			if (strstr(argv[iIndex], "-u"))
			{
				szUsername = &argv[iIndex][2];
			}
			else if (strstr(argv[iIndex], "-p"))
			{
				szPassword = &argv[iIndex][2];
			}
            else if (strstr(argv[iIndex], "-f"))
            {
                szInputFile = &argv[iIndex][2];
            }
			else if (strstr(argv[iIndex], "-P"))
			{
				szPort = &argv[iIndex][2];
			}
			else if (strstr(argv[iIndex], "--quiet"))
			{
				iInteractiveMode = 0;
			}
		}
		// assume the last parameter is the IP address
		szIPaddr = argv[argc-1];
		// convert port string to an int
		iPort = atoi(szPort);
	}
	iInteractiveMode ? printf("Connecting to API: %s:%d\n", szIPaddr, iPort) : 0;
	fdSock = apiConnect(szIPaddr, iPort);
	iLoginResult = ros_login(fdSock, szUsername, szPassword);
	if (!iLoginResult)
	{
		apiDisconnect(fdSock);
		iInteractiveMode ? printf("Invalid username or password.\n") : 0;
		exit(1);
	}
	// initialize first sentence
	initializeSentence(&stSentence);
    while (szInputFile)
    {
        iInteractiveMode ? clog("Try open commands file %s\n", szInputFile) : 0;
        FILE *f = fopen(szInputFile, "rb+");
        if (NULL == f)
        {
            iInteractiveMode ? printf("Cannot open commands file %s\n", szInputFile) : 0;
            break;
        }
        fseek(f, 0, SEEK_END);
        size_t sz = ftell(f);
        if (0 == sz)
        {
            iInteractiveMode ? printf("Commands file is too small.\n") : 0;
            fclose(f);
            break;
        }
        char *ptr = malloc(sz + 8);
        if (NULL == ptr)
        {
            iInteractiveMode ? printf("No enough memory: %zd.\n", sz) : 0;
            fclose(f);
            break;
        }
        fseek(f, 0, SEEK_SET);
        size_t rn = fread(ptr, 1, sz, f);
        fclose(f);
        if (rn != sz)
        {
            iInteractiveMode ? printf("Read file error, need %zd, but read %zd.\n", sz, rn) : 0;
            break;
        }
        *(int*)(ptr + sz) = 0;
        iInteractiveMode ? clog("Try Send commands, total %zd bytes.\n", sz) : 0;
        char *p1 = ptr;
        char *p2 = NULL;
        while (*p1 && (p2 = strchr(p1, '\n')))
        {
            *p2 = 0;
            // check to see if we want to quit
            if (strcmp(p1, "quit") == 0)
            {
                break;
            }
            // check for end of sentence (\n)
            else if (strcmp(p1, "") == 0)
            {
                // write sentence to the API
                if (stSentence.iLength > 0)
                {
                    clog("writeSentence: %d, %p\n", fdSock, &stSentence);
                    writeSentence(fdSock, &stSentence);
                    // receive and print response block from the API
                    stBlock = readBlock(fdSock);
                    printBlock(&stBlock);
                    // clear the sentence
                    clearSentence(&stSentence);
                }
            }
            // if nothing else, simply add the word to the sentence
            else
            {
                clog("addWordToSentence: <%s>\n", p1);
                addWordToSentence(&stSentence, p1);
            }
            p1 = p2 + 1;
        }
        free(ptr);
        break;
    }
	// main loop
	while (NULL == szInputFile)
	{
		// get input from stdin
		iInteractiveMode ? fputs("<<< ", stdout): 0;
		iInteractiveMode ? fflush(stdout): 0;
		if (fgets(cWordInput, sizeof cWordInput, stdin) != NULL)
		{
			szNewline = strchr(cWordInput, '\n');
			if (szNewline != NULL)
			{
				*szNewline = '\0';
			}
		}
		// check to see if we want to quit
		if (strcmp(cWordInput, "quit") == 0)
		{
			break;
		}
		// check for end of sentence (\n)
		else if (strcmp(cWordInput, "") == 0)
		{
			// write sentence to the API
			if (stSentence.iLength > 0)
			{
                clog("writeSentence: %d, %p\n", fdSock, &stSentence);
				writeSentence(fdSock, &stSentence);
				// receive and print response block from the API
				stBlock = readBlock(fdSock);
				printBlock(&stBlock);
				// clear the sentence
				clearSentence(&stSentence);
			}
		}
		// if nothing else, simply add the word to the sentence
		else
		{
            clog("addWordToSentence: <%s>\n", cWordInput);
			addWordToSentence(&stSentence, cWordInput);
		}
	}
	apiDisconnect(fdSock);
	exit(0);
}