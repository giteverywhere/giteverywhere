<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Viewing files in repository: ${repository_name}</h1>
  
  <table>
    <tr class="tr_heading">
      <th>File Name</th>
      
      
    </tr>
    %for file in view_file:
    <tr class="${loop.cycle('oddrow', 'evenrow')}">
      <td>${file['file_name']}</td>
    </tr>
    
    %endfor
  </table>
  
</div> 
