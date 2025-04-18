from django.shortcuts import render
from django.http import HttpResponse

# def myview(request):
#     # Get the current count from the session, default to 1 if not set
#     count = request.session.get('count', 1)

#     # Increment count or reset to 1 if it exceeds 4
#     count = count + 1 if count < 4 else 1
#     request.session['count'] = count  # Save the new count in session

#     # Create an HTTP response showing the count
#     response = HttpResponse(f"<h1>Session Count: {count}</h1>")

#     # Ensure the session has a session key
#     if not request.session.session_key:
#         request.session.create()

#     # Set a cookie to store the session ID
#     response.set_cookie('sessionid', request.session.session_key)

#     return response

def myview(request):
    count = request.session.get('count', 1)
    count = count + 1 if count < 4 else 1
    request.session['count'] = count

    response = HttpResponse(f"<h1>Caleb Dills View Count: {count}</h1>")
    response.set_cookie('sessionid', request.session.session_key)
    return response
