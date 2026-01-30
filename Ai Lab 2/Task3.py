# C++ has the Rule of Three and Rule of Five to make sure that objects which manage resources (like memory or files) are 
# copied, moved, and destroyed safely. If one special function is needed, the others are usually needed too.

# Python does not have these exact rules because it manages memory automatically. However, the same idea still applies. 
# When a Python class manages resources or has special behavior, related methods must be implemented together 
# (for example, __enter__ with __exit__)

# So, even though the rules are different in name and form, both C++ and Python follow the same principle: 
# if a class controls important resources or behavior, all related operations must be handled carefully and consistently.