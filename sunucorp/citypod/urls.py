from django.urls import path
from django.conf.urls import url,include

from citypod.views import viewsCategory,viewsSubCategory,viewsPage,viewsElement,viewsPublicite

from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
      #uri category
    url(r'^categories/$',viewsCategory.CategoryListView.as_view()),
    url(r'^addcategory/$',viewsCategory.CategoryCreateView.as_view()),
    url(r'^updatecategory/(?P<pk>[0-9]+)/$',viewsCategory.CategoryEditView.as_view()),
    url(r'^deletecategory/(?P<pk>[0-9]+)/$',viewsCategory.CategoryDeleteView.as_view()),
    url(r'^categorybyname/(?P<categoryName>[a-zA-Z]+)/$',viewsCategory.CategoryByNameView.as_view()),

      #uri subcategory
    url(r'^subcategories/$',viewsSubCategory.SubCategoryListView.as_view()),
    url(r'^addsubcategory/$',viewsSubCategory.SubCategoryCreateView.as_view()),
    url(r'^updatesubcategory/(?P<pk>[0-9]+)/$',viewsSubCategory.SubCategoryEditView.as_view()),
    url(r'^deletesubcategory/(?P<pk>[0-9]+)/$',viewsSubCategory.SubCategoryDeleteView.as_view()),
    url(r'^subcategorybyname/(?P<subcategoryName>[a-zA-Z]+)/$',viewsSubCategory.SubCategoryByNameView.as_view()),

    #uri element
    url(r'^elements/$',viewsElement.ElementListView.as_view()),
    url(r'^addelement/$',viewsElement.ElementCreateView.as_view()),
    url(r'^updateelement/(?P<pk>[0-9]+)/$',viewsElement.ElementEditView.as_view()),
    url(r'^deleteelement/(?P<pk>[0-9]+)/$',viewsElement.ElementDeleteView.as_view()),
    url(r'^elementbyname/(?P<elementName>[a-zA-Z]+)/$',viewsElement.ElementByNameView.as_view()),

    #uri page
    url(r'^pages/$',viewsPage.PageListView.as_view()),
    url(r'^page/$',viewsPage.PageCreateView.as_view()),
    url(r'^updatepage/(?P<pk>[0-9]+)/$',viewsPage.PageEditView.as_view()),
    url(r'^deletepage/(?P<pk>[0-9]+)/$',viewsPage.PageDeleteView.as_view()),
    url(r'^pagebyname/(?P<pageName>[a-zA-Z]+)/$',viewsPage.PageByNameView.as_view()),

      #uri page
    url(r'^pubs/$',viewsPublicite.PubliciteListView.as_view()),
    url(r'^pub/$',viewsPublicite.PubliciteCreateView.as_view()),
    url(r'^updatepub/(?P<pk>[0-9]+)/$',viewsPublicite.PubliciteEditView.as_view()),
    url(r'^deletepub/(?P<pk>[0-9]+)/$',viewsPublicite.PubliciteDeleteView.as_view()),
    url(r'^pubbyname/(?P<pubName>[a-zA-Z]+)/$',viewsPublicite.PubliciteByNameView.as_view())
]