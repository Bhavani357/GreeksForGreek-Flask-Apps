from jinja2 import Template 

name = 'Shiva'
email = 'shiva@gamil.com' 
numbers = [4,3,2,8,45,21,9,54,22,12]

File = open('templates/index_template.html', 'r')
content = File.read()
File.close()

template = Template(content)
output = template.render(name=name,email=email,numbers=numbers)

output_in_file = open('templates/index.html','w')
output_in_file.write(output) 
output_in_file.close()