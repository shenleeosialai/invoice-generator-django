from django.shortcuts import render
from . models import Invoice


def invoice_list(request):
    invoice = Invoice.objects.all()
    return render(
        request,
        'invoice/invoicegen/invoice_list.html',
        {'invoices': invoice}
    )


def invoice_detail(request, pk):
    invoice = Invoice.objects.get(pk=pk)
    return render(
        request,
        'invoice/invoicegen/invoice_detail.html',
        {'invoice': invoice}
    )