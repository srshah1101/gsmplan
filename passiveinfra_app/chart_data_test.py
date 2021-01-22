from .models import pi_siteslist,pi_siterevenues

queryset1 = pi_siteslist.objects.filter(oper_name='Airtel', ssa='AHM').all()
queryset2 = pi_siterevenues.objects.filter(oper_name='Airtel').all()
total_sum=0
for row in queryset1:
    op_rev = queryset2.get(site_id=row.site_id);
    total_sum = total_sum + (op_rev.ipfee + op_rev.ebcharge)

print("total_sum",total_sum)