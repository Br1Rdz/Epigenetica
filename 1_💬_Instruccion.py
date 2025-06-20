import streamlit as st

titulo = "Epigenetica"
st.set_page_config(page_title = titulo, 
                    page_icon = "🧬", 
                    layout = "wide",
                    initial_sidebar_state = "collapsed",
                    menu_items=None)

url = "https://github.com/Br1Rdz/"
    
markdown = """
    Developed by Bruno Rodriguez
    """
    #-------- Hide streamlit style ------------    
hide_st_style = '''
                    <style>
                    #Main Menu {visibility:hidden;}
                    footer {visibility:hidden;}
                    header {visibility:hidden;}
                    </style>
    '''
st.markdown(hide_st_style, unsafe_allow_html= True)

st.sidebar.info(markdown)
st.sidebar.info("Github: [Br1Rdz](%s)" % url)

logo = "./LOGO.png"
st.sidebar.image(logo) 
st.logo("./Informacion.png", icon_image="./info2.png")

st.markdown("<h1 style='text-align: center; color: white;'>Instrucciones</h1>", unsafe_allow_html=True)

# https://github.com/streamlit/streamlit/issues/2338

st.markdown(
    """
<div style="text-align: justify;">
    La información presentada se basa en el artículo:
    <a href="https://ashpublications.org/blood/article/137/10/1327/474571/Dynamic-CTCF-binding-directly-mediates" target="_blank" style="color:orange; text-decoration:underline;">"Dynamic CTCF binding directly mediates interactions among cis-regulatory elements essential for hematopoiesis".</a>
    Los datos utilizados para este ejemplo provienen de células madre hematopoyéticas (HSPC)
    analizadas mediante secuenciación <a href="https://www.illumina.com/techniques/multiomics/epigenetics/atac-seq-chromatin-accessibility.html" target="_blank" style="color:#e74c3c; text-decoration:underline;">ATAC-seq (Assay for Transposase-Accessible Chromatin with sequencing)</a> en los días 0 y 12.
    Además, se incorporaron datos de secuenciación  <a href="https://www.illumina.com/techniques/sequencing/dna-sequencing/chip-seq.html" target="_blank" style="color:#42c106; text-decoration:underline;">ChIP-seq (Chromatin Immunoprecipitation followed by Sequencing)</a>
    como los son el factor de transcripción <a href="https://decs.bvsalud.org/es/ths/resource/?id=50986" target="_blank" style="color:orange; text-decoration:underline;">GATA1</a> y marcas epigenéticas asociadas a estados activos (<a href="https://www.nature.com/articles/s42003-022-03099-0" target="_blank" style="color:orange; text-decoration:underline;">H3K27ac</a>)
    e inactivos (<a href="https://www.nature.com/articles/s41467-021-20940-y" target="_blank" style="color:orange; text-decoration:underline;">H3K27me3</a>) de las histonas.
    En esta aplicación, el análisis se enfocó en el <span style="color:orange;">Cromosoma 22</span> con fines prácticos, ilustrativos y educativos.
    Esta selección permite a los estudiantes explorar un subconjunto representativo de los datos y comprender mejor los conceptos clave
    detrás de las tecnologías <span style="color:#e74c3c;">ATAC-seq</span> y <span style="color:#42c106;">ChIP-seq</span>,
    así como su utilidad en el estudio de la regulación epigenética.
    Los datos de secuenciación están disponibles en el repositorio Gene Expression Omnibus (GEO) con el número de acceso <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE131055" target="_blank" style="color:orange; text-decoration:underline;">GSE131055</a>.
    <br>
    <em>Nota: Para el análisis se utilizó un subconjunto de 10 millones de lecturas de los archivos de ATAC-seq correspondientes
    a las condiciones D0 y D12, mientras que los archivos de ChIP-seq se emplearon en su totalidad.
    El procesamiento de los datos se realizó en un equipo con procesador de 4 núcleos a 2.1 GHz y 8 GB de memoria RAM.
    </em>
</div>

""", unsafe_allow_html=True
)    
    
st.markdown(
    """
<br>
<div style="text-align: justify;">
    <span style="color:orange;">Para iniciar:</span>
    <br>
    Desde la barra lateral, selecciona las distintas opciones:
    <ul>
        <li>
        <span style="color:orange;">Flujo de trabajo. </span>Esquema del flujo de trabajo.
        </li>
        <li>
        <span style="color:orange;">Resultados. </span>Visualizacion de graficos.
        </li>
        <li>
        <span style="color:orange;">Concluciones. </span>Concluciones sobre genes con regulación epigenética relacionados al Cromosoma 22.
        </li>
    </ul>
</div>
""",
    unsafe_allow_html=True
)    