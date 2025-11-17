module testbench;
    reg clk;
    reg reset;
    reg [31:0] data_in;
    wire [31:0] data_out;

    // Instantiate the simple RISC processor
    simple_risc_processor uut (
        .clk(clk),
        .reset(reset),
        .data_in(data_in),
        .data_out(data_out)
    );

    // Define coverage for data_in
    covergroup cg_data_in @(posedge clk);
        coverpoint data_in {
            bins data_in_range[] = { 0, 5, 10, 15, 20 };
        }
    endgroup

    cg_data_in cg_data_in_inst;  // Coverage instance

    // Clock generation
    always begin
        #5 clk = ~clk;  // Toggle clock every 5 time units
    end

    initial begin
        clk = 0;
        reset = 0;
        data_in = 0;
        cg_data_in_inst = new;

        // Apply reset
        reset = 1;
        #10 reset = 0;


