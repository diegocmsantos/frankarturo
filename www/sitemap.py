from django.contrib.sitemaps import Sitemap

class TipsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    
    #def items(self):
        #section = Section.objects.get(slug='dicas')
        #return Page.objects.filter(section=section)
    
    def lastmod(self, obj):
        return obj.updated_at

class SurgerySitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    
    def items(self):
        try:
            #section = Section.objects.get(slug='cirurgias')
            pass
        except Section.DoesNotExist:
            pass
        
        #return Page.objects.filter(section=section)
        return null
    
    def lastmod(self, obj):
        return obj.updated_at

class ObesitySitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    
    def items(self):
        try:
            #section = Section.objects.get(slug='obesidade')
            pass
        except Section.DoesNotExist:
            pass
        
        #return Page.objects.filter(section=section)
        return Null
    
    def lastmod(self, obj):
        return obj.updated_at
        
class ArticlesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    
    def items(self):
        try:
            #section = Section.objects.get(slug='artigos')
            pass
        except Section.DoesNotExist:
            pass
        
        #return Page.index.filter(section=section)
        return Null
    def lastmod(self, obj):
        return obj.updated_at

sitemaps = {
    'obesidade' : ObesitySitemap,
    'artigos' : ArticlesSitemap,
    'dicas' : TipsSitemap,
    'cirurgias' : SurgerySitemap
}
