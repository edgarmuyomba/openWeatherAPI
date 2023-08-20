from rest_framework import permissions 

class DiscountPerm(permissions.DjangoModelPermissions):
    message = "You do not have access to this data"

    def has_permission(self, request, view):
        if request.user.has_perm("data.3_days_3_hours"):
            return True 
        return False
    
class PremiumPerm(permissions.DjangoModelPermissions):
    message = "You are not a premium member"

    def has_permission(self, request, view):
        if request.user.has_perm("data.4_days_hourly"):
            return True 
        return False