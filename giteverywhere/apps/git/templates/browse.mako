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
   
  
   %for f in contents:
   <tr class="${loop.cycle('oddrow', 'evenrow')}">
   <td>${f['contents']}</td>
      </tr>
   %endfor  

   
      
  </table>
  
</div>
 
