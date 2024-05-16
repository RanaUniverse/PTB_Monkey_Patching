# PTB_Monkey_Patching
I made this to check on how to add different things in the python-telegram-bot 's some extenstion features.

## Here i tried to add a process so that when we will user user.full_name and the user have a < > in his name, so instead of throwing the error it will use a new property called, user.full_name_html so that it can show any error, 
##So for this i created a new class like thisngs and use the User class as a Parent class, so please check this, is this the right preocess to do this, or any other really good way, as i thinking will my code may throw any error 
