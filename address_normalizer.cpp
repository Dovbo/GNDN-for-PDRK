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
	int count1, count2, count3, count4, count5, i, spc = 0, cs1 = 0, cs2 = 0, s, f = 0;
	char add[1000], tmp[1000];
	string street_types[] = { "улица", "проспект", "проезд", "бульвар", "площадь", "переулок", "квартал", "шоссе", "пос", "тупик", "набережная", "ул.", "вулиця", "площа", "шоссе", "пр.", "набережна", "спуск", "балка", "пл.", "мкр.", "м-н", "микрорайон", "пр-т", "провулок", "шосе", "пер.", "кв.", "поселок" };
	cin.getline(add, 1000);
	string b = add;
	for (count1 = 0; count1 < strlen(add); count1++) //поиск пробелов
	{
		if (add[count1] == ' ')
		{
			spc++;
		}
	}
	s = spc * 2 - 2;
	if (spc == 0)
	{
		for (count1 = 0; count1 < 29; count1++)
		{
			b = add;
			if (b == street_types[count1])
			{
				cout << "PEREMOHA" << endl;
				break;
			}
		}
	}
	if (spc == 1)
	{
		for (count1 = 0; count1 < strlen(add); count1++)
		{
			if (add[count1] == ' ')
			{
				i = count1;
				for (count1 = 0; count1 < strlen(add); count1++)
				{
					tmp[count1] = add[count1];
				}
				tmp[i] = '\0';
			}
		}
		b = tmp;
		for (count1 = 0; count1 < 29; count1++)
		{
			if (b == street_types[count1])
			{
				cout << "PEREMOHA" << endl;
				break;
			}
		}
	}
	if (spc >= 2)
	{
		for (count1 = 0; count1 < strlen(add); count1++)
		{
			if (add[count1] == ' ')
			{
				i = count1;
				for (count1 = 0; count1 < strlen(add); count1++)
				{
					tmp[count1] = add[count1];
				}
				tmp[i] = '\0';
			}
		}
		b = tmp;
		for (count5 = 0; count5 < 29; count5++)
		{
			if (b == street_types[count5])
			{
				cout << "PEREMOHA" << endl;
				break;
			}
			if (b != street_types[count1])
			{
				for (count1 = 0; count1 < strlen(add); count1++)
				{
					if (s != 0)
					{
						s - 1;
						for (count2 = cs1; count2 < strlen(add); count2++)
						{
							if (add[count2] == ' ')
							{
								cs1 = count2;
								cs1++;
								cout << cs1 << endl;
								break;
							}
						}
					}
					if (s != 0)
					{
						s - 1;
						for (count2 = cs1; count2 < strlen(add); count2++)
						{
							if (add[count2] == ' ')
							{
								cs2 = count2;
								cs2++;
								cout << cs2 << endl;
								break;
							}
						}
						if (cs2 = cs1)
						{
							for (count2 = 0; count2 < strlen(add); count2++)
							{
								if (add[count2] == ' ')
								{
									cs2 = count2;
									cout << cs2 << endl;
									break;
								}
							}
						}
					}
					cout << cs1 << endl << cs2 << endl;
					for (count3 = cs1; count3 < cs2; count3++)
					{
						tmp[f] = add[cs1];
						f++;
					}
					tmp[cs2 + 1] = '\0';
					cout << tmp << endl;
					b = tmp;
					for (count4 = 0; count4 < 29; count4++)
					{
						if (b == street_types[count4])
						{
							cout << "PEREMOHA" << endl;
							break;
						}
						cout << 1 << endl;
					}
					f = 0;
				}
			}
		}
	}
	_getch();
    return 0;
}

