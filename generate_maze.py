//#include "stdafx.h"
#include "SnmpProtocol.h"

// helping functions
using namespace std;

// safe type conversion
unsigned int byte2int(char bb) {
	unsigned int result = 0;
	for (int i = 0; i < sizeof(unsigned int); i++) {
		result |= ((unsigned int)bb << (i * 8));
		bb >>= 8;
	}
	return result;
}

unsigned char int2byte(unsigned int number) {
	char result = 0;
	for (int i = 0; i < sizeof(unsigned int); i++) {
		result |= ((number >> (i * 8)) & 0xFF);
	}
	return result;
}

SNMP_message::SNMP_message(char* data) {
	int msg_length;
	int value_length;

	// the type byte must indicate a sequence
	if (data[0]  != Asn1DataType::SEQUENCE)
	{
		cout << "ERROR: Expected sequence (0x30) got 0x" << hex << byte2int(data[0]) << endl;
		
		error_reading_packet();

	}

	value_length =byte2int(data[1]);

	
	// skip sequence Type and Length
	data += 2;

	// read the version field
	value_length = read_tlv_int(data, this->version);

	//error check
	if (value_length < 0) // malformed packet
	{
		error_reading_packet();
	}

	// move to the next element
	data += 2 + value_length;

	//TO-DO 
	// Here goes the code to decode the SNMP messgae and fill all the fiels SNMP_message class
	


}


int  SNMP_message::to_tlv(char* ber_MSG, int max_length) {

	unsigned int total_msg_length = 0;

	//TO-DO
	// here we must perfome the BER encoding of the full message

	return total_msg_length;
}






//////////////////////////////////////////////
//BER DECODING FUNCTIONS
///////////////////////////////////////////////

// returns read bytes or -1 if error
int read_tlv_int(char *data, int &read_value)
{
	// first we check that it is actually an int
	if (byte2int(data[0]) != Asn1DataType::INTEGER )
	{
		cout << "ERROR: Expected integer value  (0x02) got 0x" << hex << byte2int(data[0]) << endl;
		return -1;
	}

	unsigned int length = byte2int(data[1]);

	read_value = byte2int(data[2]);

	return length;
}




//////////////////////////////////////////////
//BER ENCODING FUNCTIONS
///////////////////////////////////////////////

// returns  the amount of bytes written
unsigned int int_to_tlv(char *ber_coding, unsigned int value)
{
	unsigned char type= Asn1DataType::INTEGER;
	unsigned int length = sizeof(unsigned int);
	

	// always encode in 4 bytes
	ber_coding[0] = type;
	ber_coding[1] = length;
	

	for (int i = length; i >0 ; i--) {
		ber_coding[i + 2] = int2byte((value >> (i * 8)) & 0xFF);
	}
	
	return length+2;
}
