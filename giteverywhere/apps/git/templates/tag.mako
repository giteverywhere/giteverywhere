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
   <td>${tag['tag_title']}</td>
   
      </tr>
      %endfor  
  </table>
  
</div>