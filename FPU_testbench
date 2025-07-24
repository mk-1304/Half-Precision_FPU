module fp16_tb;
reg clk;reg [15:0]a,b;reg [2:0]opc;
wire [3:0]edge_case;wire [15:0] op;
integer outfile,outfile2,file_in,inputs;
fpu_16 f1(.clk(clk),.a(a),.b(b),.opc(opc),.edge_case(edge_case),.op(op));
always #50 clk = ~clk;
initial begin
clk=1;
file_in = $fopen("File Directory", "r");
if (file_in == 0) begin
$display("Error: Failed to open"); $finish; end
$display("Input file opened successfully.");
outfile = $fopen("fpu_results.txt", "w");
outfile2= $fopen("fpu_edge.txt","w");
if (!outfile) begin $display("Failed to open"); $finish; end
while(!$feof(file_in)) begin
inputs=$fscanf(file_in,"%b %b %b\n",a,b,opc);
#200
$fwrite(outfile,"%b\n",op);
#100
$fwrite(outfile2,"%b\n",edge_case);
end
$fclose(outfile);$fclose(outfile2);$finish;
end
endmodule
