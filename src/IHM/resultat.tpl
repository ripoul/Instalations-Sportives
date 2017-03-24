<h1>Resultat</h1>
<table>
<tr><th>Nom equipement</th><th>Nom installation</th><th>Adresse</th><th>CP</th><th>Ville</th></tr>
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>

<form action="http://localhost:9999/" methode="GET">
<INPUT TYPE="submit" NAME="nom" VALUE="Nouvelle recherche">

</FORM>