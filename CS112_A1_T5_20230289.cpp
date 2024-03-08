
//  program description : A game of 2 players that each player give number from 1 to 10 and add each turn to the result , who reachs 100 will be the winner.
//  version 3
//  Date of creating : 1/3/2024


#include <iostream>
using namespace std;
#include <limits>
 
int main()
{
    // welcome message 
    cout << "> > > > Welcome to \" the 100 game\" < < < <"<< endl;
    
    //  options of game:
 
   //  the main prongram:

  //  player chose option "A"
  while (true)
  {
    char option = 'A' || 'a';               // declare option variable 
    cout << "A)Start playing \nB)Exit the game "<< endl
         << "choose an option :";
    cin >> option ;  
    if (option == 'A' || option == 'a')
    {
        // Game instructions:
        cout << "<< Please read these instruction before playing >>" << endl
             << "1)Each player should choose number from 1 to 10."<< endl
             << "2)each turn will be added to the result."<< endl
             << "3)player who reachs 100 first will be the winner." << endl;
        int result =0;            // declare variable result 
        bool flag =true ;
        while (flag)
        {
            //  turn of player one:
            while (true)
            {
                int number_of_player1;
                cout <<"player 1 ,enter number from 1 to 10: ";
                cin >> number_of_player1;
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                // check if the number is valid :
                if (number_of_player1 > 0 && number_of_player1<=10)
                {
                    if (result + number_of_player1 > 100)
                    {
                        cout << "Uh oh! you  exceed 100. You lose your turn."<< endl;
                        break;
                    }
                    // check if there is a winner :
                    if (result + number_of_player1 == 100)
                    {
                        flag = false;
                        cout <<result + number_of_player1<<endl;
                        cout << "player 1 is the winner, congratulations!\nthe round is finished"<<endl;
                        break;
                    }
                    else
                    {
                        result += number_of_player1;
                        cout << "\'the result of the round now is => \'"<< result<<endl;
                        break;
                    }
                }
                else
                {
                   cout<< "put a valid number between 1 and 10"<<endl;
                }

            }
            // turn of player two:
            if (flag)
            {
                while (true)
                {
                    int number_of_player2;
                    cout <<"player 2 ,enter number from 1 to 10: ";
                    cin >> number_of_player2;
                    cin.clear();
                    cin.ignore(numeric_limits<streamsize>::max(), '\n');
                 // check if the number is valid :
                    if (number_of_player2> 0 and number_of_player2<=10)
                    {
                        if (result + number_of_player2 > 100)
                        {
                           cout << "Uh oh! you  exceed 100. You lose your turn."<< endl;
                           break;
                        }
                        // check if there a winner 
                        if (result + number_of_player2 == 100)
                        {
                           cout << result + number_of_player2 << endl;
                           cout <<" player2 is the winner, congratulations!\nthe round is finished" << endl;
                           flag = false;
                           break;
                        }
                        else
                        {
                         result += number_of_player2;
                         cout << "\'the result of the round now is => \'"<< result<<endl;
                         break;
                        }   
                    }
                    else
                    {
                        cout << "put a valid number between 1 and 10" << endl;
                    }
                }
                
            }
            
        }
        
    }
     //player chose optin "B" 
    else if (option=='B' || option== 'b')
    {
       cout << "\"Exiting the game ...Goodbye!\""<< endl;
       break;
    }
    //player chose wrong option:
    else
    {
       cout <<  "wrong option, select the right option "<< endl;
    }
 
  }

 return 0;

}
