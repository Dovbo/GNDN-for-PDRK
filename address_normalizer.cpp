// address_normalizer.cpp: ���������� ����� ����� ��� ����������� ����������.
//

#include "stdafx.h"
#include "conio.h"
#include <iostream>
#include <fstream>
#include <istream>
#include <string>
#include <windows.h>

using namespace std;

int main(int argc, char** argv)
{ 
	SetConsoleOutputCP(1251);
	SetConsoleCP(1251);
	int count, i, t;
	char add[1000], tmp[1000];
	string street_types[] = { "�����", "��������", "������", "�������", "�������", "��������", "�������", "�����", "���", "�����", "����������", "��.", "������", "�����", "�����", "��.", "���������", "�����", "�����", "��.", "���.", "�-�", "����������", "��-�", "��������", "����", "���.", "��.", "�������" };
	cin.getline(add, 1000);
	cout << strlen(add) << endl;
	string b = add;
	for (count = 0; count < strlen(add); count++)
	{
		if (add[count] == ' ')
		{
			i = count;
			cout << i << endl;
			add[i] = '\0';

		}
	}
	b = add;
	for (count = 0; count < 29; count++)
	{
		//cout << count << endl;

		if (b == street_types[count])
		{
			cout << "PEREMOHA" << endl;
			break;
		}
	}
	_getch();
    return 0;
}

