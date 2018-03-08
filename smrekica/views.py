from django.shortcuts import render, HttpResponse

def index(request):
    # preveri če je zahteva tipa POST
    if request.method == 'POST':
        #shrani podatke
        d = str(request.POST.get('number'))
        #preveri če so podatki število tipa int
        if IsInt(d) == False:
            # izpiši spletno stran smrekica/smrekica.html (v mapi templates)
            return render(request, 'smrekica/smrekica.html')
        n = int(d)
        # sestavi niz smrekica
        smrekica = ""
        for i in range (0, n):
            for j in range (0,i):
                smrekica += " "
            for k in range(0, 2 * n - (2 * i + 1)):
                smrekica += "*"
            smrekica += "\n"
            # izpiši spletno stran smrekica/smrekica2.html (templates) in za podatke pošlji niz smrekica
        return render(request, 'smrekica/smrekica2.html', {'content':smrekica})
    else:
        # izpiši spletno stran smrekica/smrekica.html (v mapi templates)
        return render(request, 'smrekica/smrekica.html')

def IsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
