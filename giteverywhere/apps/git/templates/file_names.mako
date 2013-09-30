 
<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Viewing all files of repository:${repo_name}</h1>
              
  <table>
    <tr class="tr_heading">
      
      <th>Files</th>

    </tr>
   
   %for f in f_name:
   
   <tr class="${loop.cycle('oddrow', 'evenrow')}">
    
   <td><a href="${request.route_url('git.contents',repo=repo_name, f_name=f['file_name'])}">${f['file_name']}</a></td>

   
      </tr>
      %endfor  
      
  </table>
  
</div>