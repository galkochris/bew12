1. This project is structed differently, as it uses respective app urls to seperate most different url/view locations.
        url.py is the directions the website uses to get to the views.py which run the specifc index/HttpResponse, etc.

2. we use 3 url.py files, the interact in that the main url.py from the root director moves traffic to the 2 url.py files depending
    on the app the traffic is headed to. They intereact through the include method.

3. It would be desireable to split our code when we want to have compartmentalised code for specific functions, such as users/accountholders vs visitors, or when the apps preform difference functions. We would want to do this to keep the code DRY and organized.