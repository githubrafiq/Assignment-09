from django.shortcuts import render

# Create your views here.


educations = [
        {
            'date': 'JANUARY 2003 - JANUARY 2004',
            'stage': 'Primary institute',
            'desc': 'People only remember the First and forget the Rest',
            'name': 'Nou-Bahini institute,Dhaka',
        },
        {
            'date': 'FEBRUARY 2004- DECEMBER 2006 FEBRUARY 2011- MARCH 2014',
            'stage': 'Primary & Secondary institute',
            'desc': 'The Golden moment of my Life',
            'name': 'Nou-Bahini institute,Dhaka',
        }
    ]

experiences = [
    {
        'date': 'JOCTOBER 2021 - PRESENT',
        'stage': 'Software Development Engineer',
        'desc': 'Reactjs , Python, Django',
        'name': 'Datasoft Systems Bangladesh, LTD',
    },
    {
        'date': 'FEBRUARY 2021 - SEPTEMBER 2021',
        'stage': 'Full-stack Web Developer',
        'desc': 'Nodejs, Reactjs, AWS',
        'name': 'Doodle Technologies',
    }
]

details = {
    'email': 'mahidulmoon@gmail.com',
    'phone': '+8801771042196',
    'address': "YounusKhan's scholar's Garden Ashulia Savar, Dhaka."
}

links = {
    'f': 'https://www.facebook.com/mdmahidul.moon/',
    't': '',
    'i': 'https://www.instagram.com/m4h1dul_m00n/',
    'in': 'https://www.linkedin.com/authwall?trk='
          'bf&trkInfo=AQEtgCk16MjpuAAAAX85s524nsDG2UiMvBQAs8ePGeJCDF8aoEPEmHHnTYUdmKy_'
          'iFTQdDwJHoWWuTW3HLLK015oRbO_pA_fcgGs8vcO7N-bQzc1PhxdtXupy2VNZDAkKPIsv7U=&originalReferer='
          '&sessionRedirect=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fmahidul-moon-281509144%2F',
}

context = {
    'educations': educations,
    'experiences': experiences,
    'details': details,
    'links': links,
}


def home(request):
    return render(request, 'crud/index.html', context)


def education(request):
    return render(request, 'crud/education.html', context)


def experience(request):
    return render(request, 'crud/experience.html', context)


def message(request):
    return render(request, 'crud/message.html', context)


def contact(request):
    return render(request, 'crud/contact.html', context)
