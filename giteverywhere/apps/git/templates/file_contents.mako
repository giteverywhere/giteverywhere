 
<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Viewing files of repository: </h1>  
  <table>
    <tr class="tr_heading">
      <th>Files</th>
     
    </tr>
   %for file in file_contents:
   <tr class="${loop.cycle('oddrow', 'evenrow')}">
   
   <td><a href="${request.route_url('git.contents',repo=repo , f_name=file['file_content'])}">${file['file_content']}</a></td>
   
      </tr>
      %endfor  
      
    %if directory: 
       %if repo.endswith('.db'):   
         <td>MESSAGE:Database file. Template cannot decode ASCI code</td>      
      %else:
        %for file in directory:
        <tr class="${loop.cycle('oddrow', 'evenrow')}">
        <td>${file['file_content']}</a></td>
        </tr>
         %endfor
      %endif
    %endif
  
  </table>
  
</div>