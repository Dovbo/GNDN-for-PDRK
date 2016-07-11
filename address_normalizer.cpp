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
	int count1, count2, count3, count4, count5, i, space_num = 0, spac1 = 0, spac2 = 0, spac_num_chek, f = 0;
	char add[1000], tmp[1000];
	string street_types[] = { "улица", "проспект", "проезд", "бульвар", "площадь", "переулок", "квартал", "шоссе", "пос", "тупик", "набережна€", "ул.", "вулиц€", "площа", "шоссе", "пр.", "набережна", "спуск", "балка", "пл.", "мкр.", "м-н", "микрорайон", "пр-т", "провулок", "шосе", "пер.", "кв.", "поселок" };
	cin.getline(add, 1000);
	string add_chek = add;
	for (count1 = 0; count1 < strlen(add); count1++)
	{
		if (add[count1] == ' ')
		{
			space_num++;
		}
	}
	spac_num_chek = space_num * 2 - 2;
	if (space_num == 0)
	{
		for (count1 = 0; count1 < 29; count1++)
		{
			add_chek = add;
			if (add_chek == street_types[count1])
			{
				cout << "PEREMOHA" << endl;
				break;
			}
		}
	}
	if (space_num >= 1)
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
		add_chek = tmp;
		for (count5 = 0; count5 < 29; count5++)
		{
			if (add_chek == street_types[count5])
			{
				cout << "PEREMOHA" << endl;
				break;
			}
			if (add_chek != street_types[count1])
			{
				for (count1 = 0; count1 < strlen(add); count1++)
				{
					if (spac_num_chek != 0)
					{
						spac_num_chek - 1;
						for (count2 = spac1; count2 < strlen(add); count2++)
						{
							if (add[count2] == ' ')
							{
								spac1 = count2;
								spac1++;
								cout << spac1 << endl;
								break;
							}
						}
					}
					if (spac_num_chek != 0)
					{
						spac_num_chek - 1;
						for (count2 = spac1; count2 < strlen(add); count2++)
						{
							if (add[count2] == ' ')
							{
								spac2 = count2;
								spac2++;
								cout << spac2 << endl;
								break;
							}
						}
						if (spac2 = spac1)
						{
							for (count2 = 0; count2 < strlen(add); count2++)
							{
								if (add[count2] == ' ')
								{
									spac2 = count2;
									cout << spac2 << endl;
									break;
								}
							}
						}
					}
					cout << spac1 << endl << spac2 << endl;
					for (count3 = spac1; count3 < spac2; count3++)
					{
						tmp[f] = add[spac1];
						f++;
					}
					tmp[spac2 + 1] = '\0';
					cout << tmp << endl;
					add_chek = tmp;
					for (count4 = 0; count4 < 29; count4++)
					{
						if (add_chek == street_types[count4])
						{
							cout << "PEREMOHA" << endl;
							break;
						}
					}
					f = 0;
				}
			}
		}
	}
	_getch();
    return 0;
}

