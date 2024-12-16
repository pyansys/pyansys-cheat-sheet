from ansys.workbench.core import connect_workbench

workbench = connect_workbench(port=port)
# BREAK BLOCK
host = "server_machine_name_or_IP"
port = server_port_number

workbench = connect_workbench(host=host, port=port)
# BREAK BLOCK
from ansys.workbench.core import launch_workbench

wb = launch_workbench()
# BREAK BLOCK
host = "server_machine_name_or_ip"
username = "your_username_on_server_machine"
password = "your_password_on_server_machine"

wb = launch_workbench(
    host=host, username=username, password=password
)
# BREAK BLOCK
wbjn_template = """
import os
import json
import string
import os.path
work_dir = GetServerWorkingDirectory()
arg_ProjectArchive = os.path.join(work_dir, "MatDesigner.wbpz")
# Description="Upzip the archived example project file"
Unarchive(
    ArchivePath=arg_ProjectArchive,
    ProjectPath=GetAbsoluteUserPathName(work_dir + "wbpj\\MatDesigner.wbpj"),
    Overwrite=True)
    """
wb.run_script_string(wbjn_template)
# BREAK BLOCK
wb.run_script_file("project_workflow.wbjn")
# BREAK BLOCK
import json

messages = [m.Summary for m in GetMessages()]
wb_script_result = json.dumps(messages)
# BREAK BLOCK
wb.run_script_file("project_workflow.wbjn", log_level="info")
# BREAK BLOCK
wb.upload_file("model?.prt", "*.agdb", "/path/to/some/file")
# BREAK BLOCK
wb.run_script_string(
    r"""import os
work_dir = GetServerWorkingDirectory()
geometry_file = os.path.join(work_dir, "my_geometry.agdb")
template = GetTemplate(TemplateName="Static Structural", Solver="ANSYS")
system = CreateSystemFromTemplate(Template=template, Name="Static Structural (ANSYS)")
system.GetContainer(ComponentName="Geometry").SetFile(FilePath=geometry_file)
"""
)
# BREAK BLOCK
wb.run_script_string(
    r"""import os
import shutil
work_dir = GetServerWorkingDirectory()
mechanical_dir = mechanical.project_directory
out_file_src = os.path.join(mechanical_dir, "solve.out")
out_file_des = os.path.join(work_dir, "solve.out")
shutil.copyfile(out_file_src, out_file_des)
"""
)
# BREAK BLOCK
wb.download_file("*.out")
# BREAK BLOCK
wb.download_project_archive(archive_name="my_project_archive")
# BREAK BLOCK
from ansys.mechanical.core import connect_to_mechanical

sys_name = wb.run_script_string(
    r"""import json
wb_script_result =
    json.dumps(GetTemplate(TemplateName="Static Structural (ANSYS)").CreateSystem().Name)
"""
)
server_port = wb.start_mechanical_server(
    system_name=sys_name
)
mechanical = connect_to_mechanical(
    ip="localhost", port=server_port
)
# BREAK BLOCK
import ansys.fluent.core as pyfluent

sys_name = wb.run_script_string(
    r"""import json
wb_script_result =
    json.dumps(GetTemplate(TemplateName="FLUENT").CreateSystem().Name)
"""
)
server_info_file = wb.start_fluent_server(
    system_name=sys_name
)
fluent = pyfluent.connect_to_fluent(
    server_info_file_name=server_info_file
)
# BREAK BLOCK
from ansys.sherlock.core import launcher as pysherlock

sys_name = wb.run_script_string(
    r"""import json
wb_script_result =
    json.dumps(GetTemplate(TemplateName="SherlockPre").CreateSystem().Name)
"""
)
server_port = wb.start_sherlock_server(
    system_name=sys_name
)
sherlock = pysherlock.connect_grpc_channel(
    port=server_port
)
# BREAK BLOCK
