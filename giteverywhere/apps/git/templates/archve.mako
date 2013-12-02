
<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>
</br>
</br>
<div>

  <a href="${request.route_url('git.archive', repo=repo)}">Create Zip</a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="${request.route_url('git.archive', repo=repo)}">Create tar.bz</a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="${request.route_url('git.archive', repo=repo)}">Create tar.gz</a>

  
</div>









 
 
 
 
    

   
   
