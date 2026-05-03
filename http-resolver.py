codes = {
    "100": {"name": "Continue", "description": "Request received, please continue."},
    "101": {"name": "Switching Protocols", "description": "Server is switching protocols as requested."},
    "102": {"name": "Processing", "description": "Request is being processed, no response yet."},
    "103": {"name": "Early Hints", "description": "Preliminary headers sent before final response."},

    "200": {"name": "OK", "description": "The request was successful."},
    "201": {"name": "Created", "description": "A new resource was successfully created."},
    "202": {"name": "Accepted", "description": "Request accepted but not yet processed."},
    "203": {"name": "Non-Authoritative Information", "description": "Returned metadata may be from another source."},
    "204": {"name": "No Content", "description": "Success, but no content to return."},
    "205": {"name": "Reset Content", "description": "Client should reset the document view."},
    "206": {"name": "Partial Content", "description": "Partial response due to range request."},
    "207": {"name": "Multi-Status", "description": "Multiple status codes returned for different operations."},
    "208": {"name": "Already Reported", "description": "Members already listed in a previous response."},
    "226": {"name": "IM Used", "description": "Instance manipulation applied to the response."},

    "300": {"name": "Multiple Choices", "description": "Multiple options available for the resource."},
    "301": {"name": "Moved Permanently", "description": "Resource has been permanently moved."},
    "302": {"name": "Found", "description": "Resource temporarily located at another URI."},
    "303": {"name": "See Other", "description": "Response can be found at another URI using GET."},
    "304": {"name": "Not Modified", "description": "Resource not modified since last request."},
    "305": {"name": "Use Proxy (Deprecated)", "description": "Resource must be accessed through a proxy (deprecated)."},
    "306": {"name": "(Unused)", "description": "Status code is no longer used."},
    "307": {"name": "Temporary Redirect", "description": "Temporary redirect, same method should be used."},
    "308": {"name": "Permanent Redirect", "description": "Permanent redirect, same method should be used."},

    "400": {"name": "Bad Request", "description": "Server could not understand the request."},
    "401": {"name": "Unauthorized", "description": "Authentication is required and has failed or not been provided."},
    "402": {"name": "Payment Required", "description": "Reserved for future use (payment required)."},
    "403": {"name": "Forbidden", "description": "Server understood request but refuses to authorize it."},
    "404": {"name": "Not Found", "description": "Requested resource could not be found."},
    "405": {"name": "Method Not Allowed", "description": "Request method is not supported for this resource."},
    "406": {"name": "Not Acceptable", "description": "Resource not acceptable according to request headers."},
    "407": {"name": "Proxy Authentication Required", "description": "Authentication required by a proxy."},
    "408": {"name": "Request Timeout", "description": "Server timed out waiting for the request."},
    "409": {"name": "Conflict", "description": "Request conflicts with the current state of the server."},
    "410": {"name": "Gone", "description": "Resource is no longer available and will not return."},
    "411": {"name": "Length Required", "description": "Content-Length header is required."},
    "412": {"name": "Precondition Failed", "description": "Preconditions given in request headers failed."},
    "413": {"name": "Payload Too Large", "description": "Request entity is too large."},
    "414": {"name": "URI Too Long", "description": "Request URI is too long."},
    "415": {"name": "Unsupported Media Type", "description": "Media type is not supported."},
    "416": {"name": "Range Not Satisfiable", "description": "Requested range cannot be fulfilled."},
    "417": {"name": "Expectation Failed", "description": "Server cannot meet expectation in headers."},
    "418": {"name": "I'm a Teapot", "description": "Server refuses to brew coffee because it is a teapot."},
    "421": {"name": "Misdirected Request", "description": "Request was directed at a server unable to respond."},
    "422": {"name": "Unprocessable Content", "description": "Request was well-formed but could not be processed."},
    "423": {"name": "Locked", "description": "Resource is locked."},
    "424": {"name": "Failed Dependency", "description": "Request failed due to a failed dependency."},
    "425": {"name": "Too Early", "description": "Server is unwilling to risk processing the request too early."},
    "426": {"name": "Upgrade Required", "description": "Client should switch to a different protocol."},
    "428": {"name": "Precondition Required", "description": "Request must be conditional."},
    "429": {"name": "Too Many Requests", "description": "Too many requests sent in a given time."},
    "431": {"name": "Request Header Fields Too Large", "description": "Header fields are too large."},
    "451": {"name": "Unavailable For Legal Reasons", "description": "Resource unavailable due to legal reasons."},

    "500": {"name": "Internal Server Error", "description": "Generic server error occurred."},
    "501": {"name": "Not Implemented", "description": "Server does not support the requested functionality."},
    "502": {"name": "Bad Gateway", "description": "Invalid response from upstream server."},
    "503": {"name": "Service Unavailable", "description": "Server is currently unavailable."},
    "504": {"name": "Gateway Timeout", "description": "Upstream server failed to respond in time."},
    "505": {"name": "HTTP Version Not Supported", "description": "HTTP version is not supported."},
    "506": {"name": "Variant Also Negotiates", "description": "Configuration error in content negotiation."},
    "507": {"name": "Insufficient Storage", "description": "Server cannot store the representation."},
    "508": {"name": "Loop Detected", "description": "Infinite loop detected while processing request."},
    "510": {"name": "Not Extended", "description": "Further extensions to the request are required."},
    "511": {"name": "Network Authentication Required", "description": "Client must authenticate to gain network access."}
}



import sys
import time
if len(sys.argv) < 2:
    print("Usage: http-resolver.py <code> | -l | --listrange <start> <end>")
    sys.exit()
arg = sys.argv[1]
if arg == "-l":
    for code, entry in sorted(codes.items()):
        print(f"{code} {entry['name']}: {entry['description']}")
        time.sleep(0.001)
    sys.exit()
elif arg == "--help":
    print("Usage:")
    print("  http-resolver.py <code>")
    print("  http-resolver.py -l")
    print("  http-resolver.py --listrange <start> <end>")
    sys.exit()
elif arg == "--listrange":
    if len(sys.argv) < 4:
        print("Please provide start and end range.")
        sys.exit()
    try:
        start = int(sys.argv[2])
        end = int(sys.argv[3])
    except ValueError:
        print("Range values must be integers.")
        sys.exit()
    for code, entry in sorted(codes.items()):
        code_int = int(code)
        if start <= code_int <= end:
            print(f"{code} {entry['name']}: {entry['description']}")
            time.sleep(0.001)
    sys.exit()
entry = codes.get(arg)
if entry:
    print(f"{arg} {entry['name']}: {entry['description']}")
else:
    print("Unknown status code.")