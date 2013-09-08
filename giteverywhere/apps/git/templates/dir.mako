<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Viewing all files of repository:</h1>&nbsp;
   <table>
    <tr class="tr_heading">
      <th>Directory Contents</th>
     
    </tr>
   
   %for f in browse_dir:
   
   <tr class="${loop.cycle('oddrow', 'evenrow')}">
   <td>${f['browse_dir']}</td>

   <td><a href="${request.route_url('git.browse', repo=repo)}">${f['browse_dir']}</a></td>
   
   
      </tr>
      %endfor  
      
  </table>
  
</div>
