 
<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
 %if zipped:
  ${zipped} created
 %elif tar:
   ${tar} created
 %else:
   ${tar_gz} created
 %endif
</div>









 
 
 
 
    

   
   
