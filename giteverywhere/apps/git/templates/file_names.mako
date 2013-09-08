 
<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Viewing all files of repository:${repo_name}</h1>
 

  ${repo_path}</br>
  ${d}</br>
 
            
  <table>
    <tr class="tr_heading">
      
      <th>Files</th>

    </tr>
   
   %for f in f_name:
   
<<<<<<< HEAD
   <tr class="${loop.cycle('oddrow', 'evenrow')}">
    
   <td><a href="${request.route_url('git.contents',repo=repo_name, f_name=f['file_name'])}">${f['file_name']}</a></td>
=======
   <td><a href="${request.route_url('git.contents', f_name = m)}">${f['file_name']}</a></td>
>>>>>>> 78bd82924af54c76a6ac5cc5a31f6b803b3a6013
   
      </tr>
      %endfor  
      
  </table>
  
</div>