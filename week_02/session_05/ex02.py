import sys
import io
print("Aldaanii messij", file=sys.stderr )
sys.stdout.write("Ene bol ctandart garalt\n")


sys.stderr.write("Ene bol aldaanii messej\n")

print("Ymar negen zuil biceed Enter darna uu:")
user_input =sys.stdin.readline().strip()
print(f"Ta bishcen: {user_input}")

original_stout =sys.stdout
string.io =io.StringIO()
sys.stdout= string_io
print("Ene barigdsan")
print('Ene sh bas')
 
 