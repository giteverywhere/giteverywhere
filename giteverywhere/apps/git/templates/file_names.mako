 
<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Viewing all files of repository:</h1>
 
  ${f_name}</br></br>
  ${l}</br></br>
  ${d}</br></br>
  ${a}</br></br>
  ${s}
 
  <table>
    <tr class="tr_heading">
      <th>Files</th>

    </tr>
   
   %for f in f_name:
  
   <tr class="${loop.cycle('oddrow', 'evenrow')}">
   
   
   <td><a href="${request.route_url('git.contents', f_name=d)}">${f['file_name']}</a></td>
   
      </tr>
      %endfor  
      
  </table>
  
</div>