

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
<<<<<<< HEAD

   <td><h2 style="${loop.cycle('background-color:pink;', 'background-color:lightgreen;')}">${tag['tag_title']}</h2></td>
=======
    
   <td><h2 style="${loop.cycle('background-color:red;', 'background-color:green;')}">${tag['tag_title']}</h2></td>
>>>>>>> 78bd82924af54c76a6ac5cc5a31f6b803b3a6013
   
      </tr>
      %endfor  
  </table>
  
</div>
</body>
</html>
