import base64

def decryption(code):
    base64_string = code
    decoded_bytes = base64.b64decode(base64_string)
    plain_text = decoded_bytes.decode('utf-8')
    list_of_plain_text=plain_text.split(",")
    return list_of_plain_text



dangerous="R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"
not_dangerous="RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="

list_of_dangerous=decryption(dangerous)
list_of_not_dangerous=decryption(not_dangerous)
