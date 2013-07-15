<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  
  
  <table>
    <tr class="tr_heading">
      <th>Id</th>
      <th>Name</th>
      <th>Path</th>
    </tr>
    %for c in accc2:
    <tr class="${loop.cycle('oddrow', 'evenrow')}">
      <td>${c.repo_id}</td>
      <td>${c.repo_name}</td> 
      <td>${c.repo_path}</td>
      <td><a href="${request.route_url('git.branch')}">Branches</a></td>
    
      
      
    </tr>
    %endfor
  </table>
  
</div>
 
