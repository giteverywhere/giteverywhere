

<!DOCTYPE html>
<html>
<body>
<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Viewing all tags of repository: ${repository_name}</h1>
  
  <table>
    <tr class="tr_heading">
      <th>Tags</th>
    </tr>
   %for tag in tag_list:
    
   <tr class="${loop.cycle('oddrow', 'evenrow')}">
    
   <td><h2 style="${loop.cycle('background-color:red;', 'background-color:green;')}">${tag['tag_title']}</h2></td>
   
      </tr>
      %endfor  
  </table>
  
</div>
</body>
</html>