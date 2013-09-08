 

 <%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Viewing all files of repository: ${repository_name}</h1>
  
  
  ${file_contents}
  
