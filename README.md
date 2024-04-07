# Referral-System-API
Referral System Assignment 
Referral System API Task

Objective 
The objective of this task is to build a referral system API that allows users to register, view their details, and view their referrals.

Requirements
1. User Registration Endpoint:
	* Accepts POST requests
	* Required fields: name, email, password
	* Optional field: referral\_code (if provided, the user who referred this user should receive a point)
	* Returns a unique user ID and a success message
2. User Details Endpoint:
	* Accepts GET requests
	* Requires an Authorization header with a valid token
	* Returns the user's details (name, email, referral\_code, timestamp of registration)
3. Referrals Endpoint:
	* Accepts GET requests
	* Requires an Authorization header with a valid token
	* Returns a list of users who registered using the current user's referral\_code (if any)
	* Returns a paginated response (e.g. 20 users per page)
	* Returns the timestamp of registration for each referral
