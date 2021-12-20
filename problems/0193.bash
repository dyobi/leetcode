"193. Valid Phone Numbers"

# Assume that file.txt has the following content:
# 987-123-4567
# 123 456 7890
# (123) 456-7890

# Your script should output the following valid phone numbers:
# 987-123-4567
# (123) 456-7890

# Read from the file file.txt and output all valid phone numbers to stdout.
grep -Po '^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$' file.txt