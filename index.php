<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Layton Wang</title>
    <link rel="stylesheet" type="text/css" href="stylesheet/index.css"/>
    <script type="text/javascript">
        function facultySelected() {
            var faculty = document.getElementById("fs").value;
            switch(faculty) {
                case "ar":
                    document.getElementById("cu").innerHTML = '<option value="BA(ArchStud)">BA(ArchStud)</option><option value="BA(Conservation)">BA(Conservation)</option><option value="BA(LS)">BA(LS)</option><option value="BA(UrbanStud)">BA(UrbanStud)</option><option value="Bsc(Surv)">Bsc(Surv)</option><option value="BHousMan">BHousMan</option>';
                    break;
                case "be":
                    document.getElementById("cu").innerHTML = '<option value="BBA">BBA</option><option value="BBA(Acc&Fin)">BBA(Acc&Fin)</option><option value="BBA(IBGM)">BBA(IBGM)</option><option value="BBA(IS)">BBA(IS)</option><option value="BBA(Law)">BBA(Law)</option><option value="BBA(Law)&LLB">BBA(Law)&LLB</option><option value="BEcon">BEcon</option><option value="BEcon&Fin">BEcon&Fin</option><option value="BSc(QFin)">BSc(QFin)</option>';
                    break;
                case "ed":
                    document.getElementById("cu").innerHTML = '<option value="BA&BEd(LangEd-Chin)">BA&BEd(LangEd-Chin)</option><option value="BA&BEd(LangEd-Eng)">BA&BEd(LangEd-Eng)</option><option value="BEd">BEd</option><option value="BEd&Bsc">BEd&Bsc</option><option value="BEd&BSocSc">BEd&BSocSc</option><option value="BEd(LangEd-Chin)">BEd(LangEd-Chin)</option><option value="BEd(LangEd-Eng)">BEd(LangEd-Eng)</option><option value="BSc(Exercise&Health)">BSc(Exercise&Health)</option><option value="BSc(IM)">BSc(IM)</option><option value="BSc(Sp&HearSc)">BSc(Sp&HearSc)</option>';
                    break;
                case "la":
                    document.getElementById("cu").innerHTML = '<option value="BBA(Law)&LLB">BBA(Law)&LLB</option><option value="BSocSc(Govt&Laws)&LLB">BSocSc(Govt&Laws)&LLB</option><option value="LLB">LLB</option>';
                    break;
                case "sc":
                    document.getElementById("cu").innerHTML = '<option value="BEd&Bsc">BEd&Bsc</option><option value="BSc">BSc</option><option value="BSc(ActuarSc)">BSc(ActuarSc)</option>';
                    break;
                case "art":
                    document.getElementById("cu").innerHTML = '<option value="BA(Literary Studies)">BA(Literary Studies)</option><option value="BA">BA</option><option value="BA&BEd(LangEd-Chin)">BA&BEd(LangEd-Chin)</option><option value="BA&BEd(LangEd-Eng)">BA&BEd(LangEd-Eng)</option><option value="BA&LLB">BA&LLB</option>';
                    break;
                case "de":
                    document.getElementById("cu").innerHTML = '<option value="BDS">BDS</option>';
                    break;
                case "en":
                    document.getElementById("cu").innerHTML = '<option value="BEng">BEng</option>';
                    break;
                case "me":
                    document.getElementById("cu").innerHTML = '<option value="BBiomedSc">BBiomedSc</option><option value="BChinMed">BChinMed</option><option value="BNurs">BNurs</option><option value="BPharm">BPharm</option><option value="MBBS">MBBS</option>';
                    break;
                case "ss":
                    document.getElementById("cu").innerHTML = '<option value="BEd&BSocSc">BEd&BSocSc</option><option value="BJ">BJ</option><option value="BSW">BSW</option><option value="BSocSc">BSocSc</option><option value="BSocSc(Govt&Laws)">BSocSc(Govt&Laws)</option><option value="BSocSc(Govt&Laws)&LLB">BSocSc(Govt&Laws)&LLB</option><option value="Bachelor of Criminal Justice Examination">Bachelor of Criminal Justice Examination</option>';
                    break;
                default:
                    break;
            }
        }
    </script>
</head>
<body>
    <h1></h1>
    <div class="shake">
        <h2>(`･∀･)ノ Come and subscribe your exam timetable update!!!</h2>
    </div>
    <br><br>
    <form style="text-align: center" method="post"
        action="<?php echo $_SERVER['PHP_SELF'];?>">
        <p>Name (In English): <input type="text" name="name" required="required" maxlength="20" /></p>
        <p>E-mail: <input type="text" name="email" required="required" /></p>
        <p>Faculty: <select id="fs" onchange="facultySelected()">
            <option value="ar">Architecture</option>
            <option value="be">Bussiness and Economics</option>
            <option value="ed">Education</option>
            <option value="la">Law</option>
            <option value="sc">Science</option>
            <option value="art">Arts</option>
            <option value="de">Dentistry</option>
            <option value="en">Engineering</option>
            <option value="me">Medicine</option>
            <option value="ss">Social Science</option>
        </select></p>
        <p>Curriculum: <select id="cu" required="required" name="curr">
            <option value="BA(ArchStud)">BA(ArchStud)</option>
            <option value="BA(Conservation)">BA(Conservation)</option>
            <option value="BA(LS)">BA(LS)</option>
            <option value="BA(UrbanStud)">BA(UrbanStud)</option>
            <option value="Bsc(Surv)">Bsc(Surv)</option>
            <option value="BHousMan">BHousMan</option>
        </select></p>
        <p>Course Codes: Enter course codes seperated by comma. e.g.: CAES1000, MATH2101<br>
        <textarea name="cour" required="required" 
            rows="5" cols="40" wrap="soft" maxlength="150"></textarea></p>
        <br>
        <button type="submit">submit</button>
    </form>
    <br><br>
    <?php
        $name = isset($_POST['name']) ? trim($_POST['name']) : '';
        $email = isset($_POST['email']) ? trim($_POST['email']) : '';
        $curr = isset($_POST['curr']) ? trim($_POST['curr']) : '';
        $cour = isset($_POST['cour']) ? strtoupper(trim($_POST['cour'])) : '';

        $pattern = '/^ *[A-Z]{4}[0-9]{4}( *, *[A-Z]{4}[0-9]{4} *)*$/';
        if (filter_var($email, FILTER_VALIDATE_EMAIL) && preg_match('/^( *[a-zA-Z] *)+$/', $name) && preg_match($pattern, $cour)) {
            $arr = array('name'=>$name, 'addr'=>$email, 'curr'=>$curr, 'cour'=>$cour);
            $r = json_encode($arr);
            $record = fopen("data/sub", "a") or die("Unable to open file! Please try later or contact me");
            fwrite($record, $r."\n");
            fclose($record);
            echo '<script language="javascript">';
            echo 'alert("Your subscription has been received!\nThank you for your support!")';
            echo '</script>';
        } else if ($email != '') {
            echo '<script language="javascript">';
            echo 'alert("Invalid input")';
            echo '</script>';
        }
    ?>
</body>
</html>
