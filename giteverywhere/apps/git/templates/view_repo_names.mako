 
<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <table>
    <tr class="tr_heading">
      <th>Id</th>
      <th>Name</th>
    </tr>
    %for c in view:
    <tr class="${loop.cycle('oddrow', 'evenrow')}">
    
      <td>${c.repo_id}</td>
      <td>${c.repo_name}</td> 
      
      <td><a href="${request.route_url('git.manage', repo=c.repo_name)}">Repo_Summary</a></td>
 
      
      
    </tr>
    %endfor
  </table>
  
</div>