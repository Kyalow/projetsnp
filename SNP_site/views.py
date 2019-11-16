from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from SNP_site.models import Database
from django.template import RequestContext
# Create your views here.


def home_direct(request):
    """
        Get the Home page of the application
    """
    return render_to_response("base.html")

def snp_search_redirect(request):
    """
        Redirection on snp search home page
    """
    return render_to_response("snp_search_home_page.html")

def list_phenotype_redirection(request):
    """
        Redirection on phenotype research list home page
    """

    # data_disease = Database.objects.values_list('disease', flat = True).distinct()
    # data = Database.objects.filter(disease__in = data_disease).distinct()
    data = Database.objects.values('disease', 'journal', 'date', 'first_author', 'study' ,'initial_sample_size').distinct().order_by()
    # data_disease = Database.objects.all().distinct()


    context = RequestContext(request)

    return render_to_response('phenotype_list_home.html', {"disease" : data,}, context)

def snp_search_entry(request):
    """
        Search snp entry in database
    """
    if request.method == "GET":
        query = request.GET.get('snps_id_name')
        if query:
            object_list = Database.objects.filter(snps__regex = query)
            context= RequestContext(request)
                # data = json.dumps(object_list)
            return render_to_response('SNP_search_result_page.html', {"result" : object_list,}, context)


        else:
            # when the user didn't match the database -> show a new page and put a new resaerch of SNP
            query = request.GET.get('snps_id_name_again')
            if query:
                new_match_query = Database.objects.filter(snps__regex = query)
            context = RequestContext(request)
            return render_to_response('SNP_search_result_page.html', {"result" : new_match_query }, context)


def snp_detail_entry_search(request):
    """
        create hyperlink and search in the database matched data
    """
    if request.method == "GET":
        querystring = request.GET.get('query_name') # get the query of user in result page
        result = Database.objects.filter(snps = querystring) # match the query result with Database
    context = RequestContext(request)

    return render_to_response('SNP_detail_page.html', {"result" : result}, context)

def phenotype_list_database(request):
    """
        search in database all phenotype in table with some details
    """

    data = Database.objects.values_list(disease)
    print(data)
    context = RequestContext(request)
    return render_to_response('list_pheonotype_home_page.html', {"result" : data}, context)

def phenotype_detail(request):
    """
        redirect from disease to detail desease page (phenotype + reference )
    """


    querystring = request.GET.urlencode()
    querystring = querystring.replace("+", ' ')
    querystring = querystring.replace("=", "")
    querystring = querystring.replace("%28", "(")
    querystring = querystring.replace("%29", ")")
    querystring = querystring.replace("%27", "'")
    # print(querystring)
    data = Database.objects.filter(disease = querystring).values('disease', 'link').distinct() # get the query without occurency of the same item
    # data = Database.objects.values('disease', 'reference')
    # print(data)
    context = RequestContext(request)

    return render_to_response('phenotype_detail_page.html', {"result" : data}, context)
