# Get user email address
email = input("What is your email address?: ").strip()

# Slice out the user name
user_name = email[:email.index("@")]

# Slice the domain name
domain_name = email[email.index("@")+1:]

# Format message
output = f"your user name is {user_name} \n your domain name is {domain_name}"

# Display output message
print(output)
