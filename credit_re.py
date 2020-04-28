#Note:-
# to test git on 04282020
# to test git on 04282020_2
# Condition - "It must NOT have 4 or more consecutive repeated digits" is not satsfied with this program. 
# To satisfy above condition, need other program. With the help of google I found some program and after some tweakings
# that's working as well for me. Not sharing that because it's not my original work.
import re
credit = ["4123456789123456", "5123-4567-8912-3456", "61234-567-8912-3456", "4123356789123456", "5133-3367-8912-3456", "5123 - 3567 - 8912 - 3456"]
PATTERN='^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'
for i in credit:
    match = re.match(PATTERN, i)
    if match:
        print "Valid" #match.group()
    else:
        print "Invalid"
