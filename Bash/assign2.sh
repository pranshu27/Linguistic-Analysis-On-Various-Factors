SECONDS=0


./percent-india.sh   
echo "executed  percent-india.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""

./gender-india.sh  
echo "executed gender-india.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
./geography-india.sh                  
echo "executed geography-india.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
./3-to-2-ratio.sh
echo "executed 3-to-2-ratio.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
./2-to-1-ratio.sh
echo "executed 2-to-1-ratio.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
./age-india.sh 
echo "executed age-india.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
./literacy-india.sh
echo "executed literacy-india.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
./region-india.sh
echo "executed region-india.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
./age-gender.sh
echo "executed age-gender.sh"


duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
./literacy-gender.sh
echo "executed literacy-gender.sh"

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
echo ""
echo "Finished. Please check the resultant CSV files."
