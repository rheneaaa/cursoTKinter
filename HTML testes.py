pagina = open("index.html", "w")
pagina.write("<html lang='pt-BR'>\n")
pagina.write("<head>\n")
pagina.write("<title>Página em HTML com Python</title>\n")
pagina.write("</head>\n")
pagina.write("<body>\n")
pagina.write("Listar contagem de 10 números\n")
for l in range(10):
    pagina.write("<p>%d</p>\n" % l)
pagina.write("</body>\n")
pagina.write("</html>\n")
pagina.close()
