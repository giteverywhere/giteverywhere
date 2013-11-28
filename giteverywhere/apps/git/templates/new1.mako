
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
  
   %for u in unc:
     <tr class="${loop.cycle('oddrow', 'evenrow')}"> 
     %if (u['unc_title']).startswith ('+'):
       <td style="background-color:lightgreen">${u['unc_title']}</td>
     %elif (u['unc_title']).startswith ('-'):
       <td style="background-color:pink">${u['unc_title']}</td>
     %else:
       <td style="background-color:white">${u['unc_title']}</td>
     </tr>
     %endif
  %endfor
 
 </table>
</div>
</body>
</html> 
 
