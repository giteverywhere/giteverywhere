 
<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Viewing all files of repository:</h1>
  
  <table>
    <tr class="tr_heading">
      <th>Files</th>

    </tr>
   %for f in file_names:
   <tr class="${loop.cycle('oddrow', 'evenrow')}">

 
   <td><a href="${request.route_url('git.contents', f_name=file_names)}">${f['file_name']}</a></td>

   
      </tr>
      %endfor  
  </table>
  
</div>