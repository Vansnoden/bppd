import BarChart from "../ui/dashboard/charts/barchart";
import CardWrapper from "../ui/dashboard/card";
import { lusitana } from "../ui/fonts";
import { getDashboardData, getPlantTopX, getRegionObsDistro } from "../lib/actions";
import DataTable from "../ui/dashboard/table";
import Search from "../ui/dashboard/search";
import PieChart from "../ui/dashboard/charts/piechart";



export default async function Dashboard(props: {
    searchParams?: Promise<{
      query?: string;
      page?: string;
    }>;
  }){  

    const dashData = await getDashboardData("");
    const plantTop = await getPlantTopX("", 10); //global
    const regionObsDistro = await getRegionObsDistro(""); // global
    const searchParams = await props.searchParams;
    const query = searchParams?.query || '';
    const currentPage = Number(searchParams?.page) || 1;

    return(
        <div>
            <h1 className={`${lusitana.className} mb-4 text-xl md:text-2xl`}>
                Dashboard
            </h1>
            <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
                <CardWrapper total_plants={dashData?.total_plants} total_sites={dashData?.total_sites}/>
            </div>
            <div className="py-3 mt-3 grid gap-6 sm:grid-cols-1 md:grid-cols-4">
                <div>
                    <h2 className={`${lusitana.className} mb-2`}>
                        Quick Stats
                    </h2>
                    <div>
                        <BarChart data={plantTop} show_labels={false}/>
                    </div>
                    <div>
                        <PieChart data={regionObsDistro} width={300} show_labels={false} />
                    </div>
                </div>
                <div className="sm:col-span-4 md:col-span-3">
                    <Search placeholder="Search ..." />
                    <DataTable query={query} currentPage={currentPage}/>
                </div>
            </div> 
        </div>
    )
}