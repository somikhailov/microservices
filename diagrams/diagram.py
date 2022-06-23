from diagrams import Cluster, Diagram, Edge
from diagrams.k8s.compute import Deployment, Pod
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.storage import PV, PVC

with Diagram("microservices", show=False):

    ing = Ingress("app.somikhailov.fun")

    with Cluster("vue-client"):      
        s_vue = Service("vue")
        Deployment("vue") >> Edge(color="red") >> s_vue >>  Edge(color="blue") << ing 

    with Cluster("flask-backend"):
        s_flask = Service("flask")
        ing >> Edge(color="blue") >> s_flask >> Edge(color="darkgreen") << Deployment("flask") 

    s_vue >> Edge(color="red") >> s_flask 

    with Cluster("postgres-db"):
        PV("postgres-pv") << PVC("postgres-pvc") << Deployment("postgres") << Service("postgres") << s_flask 
